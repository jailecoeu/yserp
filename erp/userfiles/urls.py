# coding: utf-8
#__author__ = 'chang'
#__create__ = '上午11:21'
from django.conf.urls import patterns,url

urlpatterns = patterns('userfiles.views',
    url(r'^upload/$', 'upload',name='userfiles_upload'),
    (r'^upload/swf/$', 'upload_swf'),
    url(r'^upload/test/$', 'upload_test',name='userfiles_upload_test'),
    (r'^ueditor/controller/$', 'ueditor_controller'),
    (r'^ueditor/upload/$', 'ueditor_upload'),
)