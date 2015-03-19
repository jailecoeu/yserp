# coding: utf-8
#__author__ = 'chang'
#__create__ = '下午1:55'
from django.conf.urls import patterns, url

urlpatterns = patterns('carsales.views.pages',
    url(r'^list/$', 'order_list', name='carsales_order_list'),
    url(r'^create/$', 'order_create', name='carsales_order_create'),
    url(r'^api/order/edit/(?P<id>\d+)/$','order_edit',name='carsales_order_edit'),

)

urlpatterns += patterns('carsales.views.api',
    (r'^api/order/create/$','order_create'),
)