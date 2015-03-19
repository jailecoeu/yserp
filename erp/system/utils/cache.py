# coding: utf-8
#__author__ = 'chang'
#__create__ = '15-3-6'
from system.models import *

def get_currency_list():
    '''获取币种列表'''
    return Currency.objects.only('id','name').filter(state=0).order_by('sort')

def get_customer_list():
    '''获取客户列表'''
    return Customer.objects.only('id','name').filter(state=0)

def get_supplier_list():
    '''获取供应商列表'''
    return Supplier.objects.only('id','name').filter(state=0).order_by('sort')

def get_dealer_list():
    '''获取经销商列表'''
    return Dealer.objects.only('id','name').filter(state=0).order_by('sort')

def get_agency_list():
    '''获取代理商列表'''
    return Agency.objects.only('id','name').filter(state=0).order_by('sort')

def get_shipping_list():
    '''获取船运公司列表'''
    return Shipping.objects.only('id','name').filter(state=0).order_by('sort')

def get_logistics_list():
    '''获取物流公司列表'''
    return Logistics.objects.only('id','name').filter(state=0).order_by('sort')

def get_port_list():
    '''获取港口列表'''
    return Port.objects.only('id','name').filter(state=0).order_by('sort')

def get_showroom_list():
    '''获取展厅列表'''
    return Showroom.objects.only('id','name').filter(state=0).order_by('sort')


def get_car_brand_list():
    '''获取汽车品牌列表'''
    objs = CarType.objects.values('brand').filter(state=0).distinct()
    data_list = [
        {
            'name':obj['brand']
        } for obj in objs
    ]
    return data_list

def get_car_series_list(brand):
    '''获取汽车系列'''
    objs = CarType.objects.values('series').filter(state=0,brand=brand).distinct()
    data_list = [
        {
            'name':obj['series']
        } for obj in objs
    ]
    return data_list

def get_car_series_no_list(brand, series):
    '''获取汽车车型'''
    objs = CarType.objects.values('series_no').filter(state=0,brand=brand,series=series).distinct()
    data_list = [
        {
            'name':obj['series_no']
        } for obj in objs
    ]
    return data_list

def get_car_years_list(brand,series,series_no):
    '''获取汽车年款'''
    objs = CarType.objects.values('years').filter(state=0,brand=brand,series=series,series_no=series_no).distinct()
    data_list = [
        {
            'name':obj['years']
        } for obj in objs
    ]
    return data_list

def get_car_conf_list(brand,series,series_no,years):
    '''获取汽车配置'''
    objs = CarType.objects.values('conf').filter(state=0,brand=brand,series=series,series_no=series_no,years=years).distinct()
    data_list = [
        {
            'name':obj['conf']
        } for obj in objs
    ]
    return data_list

def get_car_version_list(brand,series,series_no,years,conf):
    '''获取汽车版本'''
    objs = CarType.objects.values('id','version').filter(state=0,brand=brand,series=series,series_no=series_no,
                                                      years=years,conf=conf)
    data_list = [
        {
            'id':obj['id'],
            'name':obj['version']
        } for obj in objs
    ]
    return data_list