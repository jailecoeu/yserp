# coding: utf-8
#__author__ = 'chang'
#__create__ = '15-3-3'
import copy
import uuid
from django.template.response import TemplateResponse
from account.decorators import login_required
from pagination.decorators import paginate
from carsales.models import CarOrder
from system.utils import cache as system_cache

@login_required
@paginate
def order_list(request):
    '''
    综合查询
    '''
    data = {}
    brand = request.GET.get('brand','')
    series = request.GET.get('series','')
    series_no = request.GET.get('series_no','')
    vin = request.GET.get('vin','')
    engine_no = request.GET.get('engine_no','')
    customer = int(request.GET.get('customer',0))
    order_no = request.GET.get('order_no','')
    supplier_no = request.GET.get('supplier_no','')

    order_objs = CarOrder.objects.filter(state=0)

    #筛选
    if brand:
        order_objs = order_objs.filter(car_type__brand=brand)
    if series:
        order_objs = order_objs.filter(car_type__series=series)
    if series_no:
        order_objs = order_objs.filter(car_type__series_no=series_no)
    if vin:
        order_objs = order_objs.filter(vin__icontains=vin)
    if engine_no:
        order_objs = order_objs.filter(engine_no=engine_no)
    if order_no:
        order_objs = order_objs.filter(order_no=order_no)
    if supplier_no:
        order_objs = order_objs.filter(supplier_no=supplier_no)
    if customer:
        order_objs = order_objs.filter(customer_id=customer)

    #基础数据
    data['brand_list'] = system_cache.get_car_brand_list()
    data['series_list'] = system_cache.get_car_series_list(brand) if brand else []
    data['series_no_list'] = system_cache.get_car_series_no_list(brand,series) if (brand and series) else []
    data['customer_list'] = system_cache.get_customer_list()

    #查询数据
    data['total_count'] = order_objs.count()
    data['orders'] = order_objs

    #查询参数
    data['s_brand'] = brand
    data['s_series'] = series
    data['s_series_no'] = series_no
    data['s_vin'] = vin
    data['s_engine_no'] = engine_no
    data['s_order_no'] = order_no
    data['s_supplier_no'] = supplier_no
    data['s_customer'] = customer

    return TemplateResponse(request,'carsales/order_list.html',data)



@login_required
def order_create(request):
    '''
    新建项目
    '''
    data = {}

    #基础数据
    data['brand_list'] = system_cache.get_car_brand_list()
    data['supplier_list'] = system_cache.get_supplier_list()
    data['customer_list'] = system_cache.get_customer_list()
    data['currency_list'] = system_cache.get_currency_list()

    data['no'] = str(uuid.uuid1()).replace('-','')


    return TemplateResponse(request,'carsales/order_edit.html',data)

@login_required
def order_edit(request,id):
    '''
    订单修改
    '''
    data = {}

    #基础数据
    data['brand_list'] = system_cache.get_car_brand_list()
    data['supplier_list'] = system_cache.get_supplier_list()
    data['customer_list'] = system_cache.get_customer_list()
    data['currency_list'] = system_cache.get_currency_list()
    data['port_list'] = system_cache.get_port_list()
    data['shipping_list'] = system_cache.get_shipping_list()
    data['showroom_list'] = system_cache.get_showroom_list()
    data['agency_list'] = system_cache.get_agency_list()

    #页面数据
    car_order = CarOrder.objects.get(id=id,state=0)
    data['car_order'] = car_order

    return TemplateResponse(request,'carsales/order_edit.html',data)