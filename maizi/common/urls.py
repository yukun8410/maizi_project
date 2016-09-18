#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
common模块的url配置。
"""

from django.conf.urls import patterns, url
from django import views

urlpatterns = patterns('common.views',
    url(r'^$', 'index', name='index'),
    url(r'^ad/(?P<path>.*)$', views.static.serve, {'document_root': 'images/ad/'}),
)
