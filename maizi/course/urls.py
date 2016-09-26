#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
course模块的url配置。
"""
from django.contrib import admin
from course import views
from django.conf.urls import include, url
from common.urls import url
from django.conf.urls import patterns

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('common.urls')),
]
