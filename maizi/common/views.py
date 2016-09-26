#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""

from django.shortcuts import render, redirect
from common.models import *
from django.http import JsonResponse, HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from random import Random
from django.contrib.auth.hashers import make_password
import django.utils.timezone


# 首页
def index(request):
    # 搜索关键字
    rekeywords = RecommendKeywords.objects.all()
    # 广告列表
    ad_list = Ad.objects.order_by("-index")
    # 最新课程
    new_course_list = Course.objects.order_by("-date_publish")
    # 最多播放课程
    play_course_list = Course.objects.order_by("-click_count")
    # 最具人气课程
    favorite_course_list = Course.objects.order_by("-favorite_count")
    # 名师风采
    teacher_list = UserProfile.objects.filter(groups__name="老师")
    # 推荐新闻(官方活动)
    reading_av = RecommendedReading.objects.filter(reading_type='AV')
    # 推荐新闻（开发者资讯）
    reading_news = RecommendedReading.objects.filter(reading_type='NW')
    # 推荐新闻（技术交流）
    reading_dc = RecommendedReading.objects.filter(reading_type='DC')
    # 友情链接(图片链接)
    pic_links = Links.objects.filter(is_pic=1)
    # 友情链接（非图片）
    links = Links.objects.filter(is_pic=0)
    return render(request, "common/index.html", locals())


# 课程关键字搜索
def careercourse(request):
    info_text = request.GET.get('com_input', None)
    info_data = Keywords
    info = info_data.objects.get(name=info_text)
    careercourse = info.careercourse_set.all()
    careercourse_list = []
    for inf in careercourse:
        img = str(inf.image)
        careercourse_list.append({'info': inf.name, 'img': img})
        return JsonResponse(careercourse_list, safe=False)


# 小课程搜索
def small_course(request):
    info_text = request.GET.get('com_input', None)
    info_data = Keywords
    info = info_data.objects.get(name=info_text)
    course = info.course_set.all()
    course_list = []
    for inf in course:
        course_list.append({'info': inf.name})
        return JsonResponse(course_list, safe=False)


# 登录及验证
def login_check(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request.META['HTTP_REFERER'])
    else:
        return JsonResponse({'info': 'None'}, safe=False)


# 注销
def logout_user(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])


# 注册用户并登录
def register(request):
    user_email = request.GET.get('username', None)
    user_pass = request.GET.get('password', None)
    user = UserProfile.objects.filter(username=user_email).exists()
    # print user
    if user is True:
        return JsonResponse({'info': 'exist'}, safe=False)
    else:
        user_reg = UserProfile.objects.create_user(user_email, password=make_password(user_pass, None, 'pbkdf2_sha256'))
        user_reg.save()
        user_reg.backend = 'django.contrib.auth.backends.ModelBackend'  # 声名使用哪个后台验证模块去做登录验证
        login(request, user_reg)
        return JsonResponse({'info': 'ok'}, safe=False)


# 自动生成找回密码的链接验证码方法
def random_str(randomlength=10):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


# 账号密码找回, 发送认证链接
def forgot_password(request):
    user_email = request.GET.get('username', None)
    user = UserProfile.objects.filter(username=user_email).exists()
    if user is False:
        return JsonResponse({'info': 'non-existent'}, safe=False)
    else:
        bcode = random_str()
        record = EmailVerifyRecord.objects.create(code=bcode, email=user_email, type=1, ip=request.META['REMOTE_ADDR'])
        record.save()
        message = u'请打开链接重置密码'+"\n"+"http://127.0.0.1:8000/find_pass/"+ bcode
        send_mail('用户密码找回认证',message, 'rxdyh12@126.com', [user_email], fail_silently=True)
        return JsonResponse({'info': 'ok'}, safe=False)


# 修改密码前期处理
def find_pass(request, bcode):
    change_status = EmailVerifyRecord.objects.filter(code=bcode)
    if change_status.exists() is True:
        email = change_status.values('email').first()['email']
        create_time = change_status.values('created').first()['created']
        time_now = django.utils.timezone.now()
        time = time_now-create_time
        if time.days >= 1:
            return render(request, 'common/find_pwd_error.html', locals())
        else:
            user_info = UserProfile.objects.filter(username=email).first()
            return render(request, 'common/changepass.html', locals())
    else:
        return render(request, 'common/find_pwd_error.html', locals())


# 修改密码后端处理
def change_find_pass(request):
    user_email = request.GET.get('username', None)
    new_password = request.GET.get('password', None)
    user_info = UserProfile.objects.filter(username=user_email)
    user_info.password = make_password(new_password, None, 'pbkdf2_sha256')
    user_info.update()
    return JsonResponse({'info': 'ok'}, safe=False)

