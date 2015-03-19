# coding: utf-8
#__author__ = 'chang'
#__create__ = '下午1:28'
from django.conf.urls import patterns, url

urlpatterns = patterns('system.views.api',
    (r'^api/car/brand/$', 'car_brand'),
    (r'^api/car/series/$', 'car_series'),
    (r'^api/car/series_no/$', 'car_series_no'),
    (r'^api/car/years/$', 'car_years'),
    (r'^api/car/conf/$', 'car_conf'),
    (r'^api/car/version/$', 'car_version'),
)
