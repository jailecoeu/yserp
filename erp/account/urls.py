# coding: utf-8
#__author__ = 'chang'
#__create__ = '下午4:26'
from django.conf.urls import patterns, url

urlpatterns = patterns('account.views',
    url(r'^login/$', 'login', name='account_login'),
    url(r'^logout/$', 'logout', name='account_logout'),
)