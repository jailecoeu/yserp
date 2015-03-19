# coding: utf-8
#__author__ = 'chang'
#__create__ = '14-12-18'
from django.contrib import admin
from userfiles.models import UFile

class UFileAdmin(admin.ModelAdmin):

    list_display = ('id','fpath','ftype','xsize','ysize','msize','user', 'create_time')
    search_fields = ('fpath','desc')
    raw_id_fields = ('user',)
    list_per_page = 50
    list_filter = ('create_time', 'state')

admin.site.register(UFile, UFileAdmin)