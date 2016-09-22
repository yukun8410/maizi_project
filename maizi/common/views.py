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
from django.contrib.auth import authenticate,login,logout
import json
from django.contrib.auth.hashers import make_password,check_password



# 首页
def index(request):
    rekeywords = RecommendKeywords.objects.all()
    ad_list = Ad.objects.order_by("-index")

    return render(request, "common/index.html", locals())


# 课程关键字搜索
def careercourse(request):
    info_text = request.GET.get('com_input', None)
    info_data = Keywords
    info = info_data.objects.get(name=info_text)
    careercourse = info.careercourse_set.all()
    # course = info.course_set.all()
    careercourse_list = []
    # course_list=[]
    for inf in careercourse:
        img = str(inf.image)
        careercourse_list.append({'info': inf.name, 'img': img})
        return JsonResponse(careercourse_list, safe=False)


def small_course(request):
    info_text = request.GET.get('com_input', None)
    info_data = Keywords
    info = info_data.objects.get(name=info_text)
    course = info.course_set.all()
    course_list = []
    for inf in course:
        course_list.append({'info': inf.name})
        return JsonResponse(course_list, safe=False)


def login_check(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request.META['HTTP_REFERER'])
        # return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return JsonResponse({'info': 'None'}, safe=False)


def logout_user(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])


def register(request):
    pass