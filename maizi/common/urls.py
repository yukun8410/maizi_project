#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
common模块的url配置。
"""
import common
import django
from django.conf.urls import patterns, url
from django import views
from common.views import *
# urlpatterns = patterns('common.views',
#     url(r'^$', 'index', name='index'),
#     url(r'^ad/(?P<path>.*)$', views.static.serve, {'document_root': 'images/ad/'}),
# )


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^ad/(?P<path>.*)$', django.views.static.serve, {'document_root': 'images/ad/'}),
    url(r'^login_check/$', login_check, name='login_check'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^forgot_password/$', forgot_password, name='forgot_password'),
    url(r'^find_pass/(?P<bcode>[\w\d+]{10})/$', find_pass, name='find_pass'),
    url(r'^change_find_pass/$', change_find_pass,name='change_find_pass'),
    url(r'^careercourse/$', careercourse, name='careercourse'),
    url(r'^small_course/$', small_course, name='small_course'),
    url(r'^course_img/(?P<path>.*)$', django.views.static.serve, {'document_root': 'images/course_img/'}),
        ]

