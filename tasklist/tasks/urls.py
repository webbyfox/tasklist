# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^task/(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    url(r'^task/new/$', views.task_new, name='task_new'),
]
