# coding: utf-8
#__author__ = 'chang'
#__create__ = '15-3-3'
import copy
import ujson as json

from django.template.response import HttpResponse
from system import settings
from system.models import CarType
from system.utils import cache as system_cache

def car_brand(request):
    '''
    品牌
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    rsp_data['data'] = {}

    brand_list = system_cache.get_car_brand_list()

    rsp_data['data']['brand'] = brand_list

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')


def car_series(request):
    '''
    车系
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    rsp_data['data'] = {}

    brand = request.GET.get('brand','')
    series_list = system_cache.get_car_series_list(brand)
    rsp_data['data']['series'] = series_list

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')

def car_series_no(request):
    '''
    车型
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])

    rsp_data['data'] = {}

    brand = request.GET.get('brand','')
    series = request.GET.get('series','')
    series_no_list = system_cache.get_car_series_no_list(brand,series)
    rsp_data['data']['series_no'] = series_no_list

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')

def car_years(request):
    '''
    年款
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])

    rsp_data['data'] = {}
    brand = request.GET.get('brand','')
    series = request.GET.get('series','')
    series_no = request.GET.get('series_no','')

    years_list = system_cache.get_car_years_list(brand,series,series_no)
    rsp_data['data']['years'] = years_list

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')

def car_conf(request):
    '''
    配置
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    rsp_data['data'] = {}
    brand = request.GET.get('brand','')
    series = request.GET.get('series','')
    series_no = request.GET.get('series_no','')
    years = request.GET.get('years','')

    conf_list = system_cache.get_car_conf_list(brand,series,series_no,years=years)
    rsp_data['data']['conf'] = conf_list

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')

def car_version(request):
    '''
    版本
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    rsp_data['data'] = {}
    brand = request.GET.get('brand','')
    series = request.GET.get('series','')
    series_no = request.GET.get('series_no','')
    years = request.GET.get('years','')
    conf = request.GET.get('conf','')

    version_list = system_cache.get_car_version_list(brand,series,series_no,years=years,conf=conf)
    rsp_data['data']['version'] = version_list

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')

