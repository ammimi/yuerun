#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import url
from accounts import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.AccountsList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.AccountDetail.as_view()),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)