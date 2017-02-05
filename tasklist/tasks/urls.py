# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from .models import Task
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^api/$', views.task_list),
    url(r'^api/(?P<pk>[0-9]+)/$', views.task_detail),
    url(r'^api/delete/(?P<pk>[0-9]+)/$', views.task_detail),
    url(r'^api/current_user/$', views.current_user),
    # url(r'^task/new/$', views.task_new, name='task_new'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
