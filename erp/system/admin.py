#coding: utf-8
from django.contrib import admin
from system.models import Supplier,Dealer,Agency,Shipping,Logistics,Showroom,Customer,Port,\
                            KwDict,Currency,CarType

class KwDictAdmin(admin.ModelAdmin):
    ''''''
    list_display = ('id','name')
    list_filter = ('state','code')

#admin.site.register(KwDict,KwDictAdmin)

class CustomerAdmin(admin.ModelAdmin):
    ''''''
    list_display = ('id','name')
    list_filter = ('state',)

admin.site.register(Customer,CustomerAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    ''''''
    list_display = ('id','name','rate')
    list_filter = ('state',)

admin.site.register(Currency,CurrencyAdmin)


class SupplierAdmin(admin.ModelAdmin):
    '''供货商'''
    list_display = ('id','name')
    list_filter = ('state',)

admin.site.register(Supplier,SupplierAdmin)

class DealerAdmin(admin.ModelAdmin):
    '''经销商'''
    list_display = ('id','name')
    list_filter = ('state',)

admin.site.register(Dealer,DealerAdmin)


class AgencyAdmin(admin.ModelAdmin):
    '''代理公司'''
    list_display = ('id','name')
    list_filter = ('state',)

admin.site.register(Agency,AgencyAdmin)

class ShippingAdmin(admin.ModelAdmin):
    '''船运公司'''
    list_display = ('id','name')
    list_filter = ('state',)

admin.site.register(Shipping,ShippingAdmin)

class LogisticsAdmin(admin.ModelAdmin):
    '''物流公司'''
    list_display = ('id','name')
    list_filter = ('state',)

admin.site.register(Logistics,LogisticsAdmin)

class PortAdmin(admin.ModelAdmin):
    '''港口'''
    list_display = ('id','name')
    list_filter = ('state',)

admin.site.register(Port,PortAdmin)

class ShowroomAdmin(admin.ModelAdmin):
    '''展厅'''
    list_display = ('id','name')
    list_filter = ('state',)

admin.site.register(Showroom,ShowroomAdmin)


class CarTypeAdmin(admin.ModelAdmin):
    '''车型'''
    list_display = ('id','brand','series','series_no','years','conf','version')
    list_filter = ('state',)

admin.site.register(CarType,CarTypeAdmin)