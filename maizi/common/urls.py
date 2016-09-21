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
from common import views
# urlpatterns = patterns('common.views',
#     url(r'^$', 'index', name='index'),
#     url(r'^ad/(?P<path>.*)$', views.static.serve, {'document_root': 'images/ad/'}),
# )


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ad/(?P<path>.*)$', django.views.static.serve, {'document_root': 'images/ad/'}),
    url(r'^login_check/$', common.views.login_check, name='login_check'),
    url(r'^register/$', views.register, name='register'),
    url(r'^careercourse/$', views.careercourse, name='careercourse'),
    url(r'^small_course/$', views.small_course, name='small_course'),
    url(r'^course_img/(?P<path>.*)$', django.views.static.serve, {'document_root': 'images/course_img/'}),
        ]

