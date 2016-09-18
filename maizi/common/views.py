#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""

from django.shortcuts import render
from common.models import *

# 首页
def index(request):
    rekeywords = RecommendKeywords.objects.all()
    ad_list = Ad.objects.order_by("-index")

    return render(request, "common/index.html", locals())
