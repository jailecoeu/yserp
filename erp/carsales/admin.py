#coding: utf-8
from django.contrib import admin
from carsales.models import *

class CarOrderAdmin(admin.ModelAdmin):
    '''汽车订单'''
    list_display = ('id','order_no')
    list_filter = ('state',)

admin.site.register(CarOrder,CarOrderAdmin)

class Step2Admin(admin.ModelAdmin):
    '''开证阶段'''
    list_display = ('id','car_order')
    list_filter = ('state',)
    raw_id_fields = ('car_order',)

admin.site.register(Step2,Step2Admin)

class Step3Admin(admin.ModelAdmin):
    '''起运阶段'''
    list_display = ('id','car_order')
    list_filter = ('state',)
    raw_id_fields = ('car_order',)

admin.site.register(Step3,Step3Admin)


class Step4Admin(admin.ModelAdmin):
    '''到港阶段'''
    list_display = ('id','car_order')
    list_filter = ('state',)
    raw_id_fields = ('car_order',)

admin.site.register(Step4,Step4Admin)


class Step5Admin(admin.ModelAdmin):
    '''报关阶段'''
    list_display = ('id','car_order')
    list_filter = ('state',)
    raw_id_fields = ('car_order',)

admin.site.register(Step5,Step5Admin)