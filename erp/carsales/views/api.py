# coding: utf-8
#__author__ = 'chang'
#__create__ = '15-3-6'
import copy
import ujson as json
from django.template.response import HttpResponse
from django.contrib import auth
from account.decorators import login_required
from carsales.models import *
from carsales import settings


@login_required
def order_create(request):
    '''新建项目--海外订车'''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    uid = request.session[auth.SESSION_KEY]
    no = request.POST['no']
    supplier = int(request.POST['supplier'])
    supplier_no = request.POST['supplier_no']
    customer = request.POST['customer']
    order_no = request.POST['order_no']
    seat_num = request.POST['seat_num']
    key_num = request.POST['key_num']
    car_type = request.POST['car_type']
    car_type_remark = request.POST['car_type_remark']
    made_time = request.POST['made_time']
    vin = request.POST['vin']
    engine_no = request.POST['engine_no']
    tire_size = request.POST['tire_size']
    price = int(request.POST['price'])
    currency = int(request.POST['currency'])
    rate = float(request.POST['rate'])
    overseas_deposit = request.POST['overseas_deposit']
    china_deposit = request.POST['china_deposit']
    contract_money = request.POST['contract_money']

    try:
        CarOrder.objects.create(no=no,order_registrant_id=uid,supplier_id=supplier,supplier_no=supplier_no,customer_id=customer,order_no=order_no,
                                seat_num=seat_num,key_num=key_num,car_type_id=car_type,car_type_remark=car_type_remark,made_time=made_time,vin=vin,
                                engine_no=engine_no,tire_size=tire_size,price=price,currency_id=currency,rate=rate,
                                overseas_deposit=overseas_deposit,china_deposit=china_deposit,contract_money=contract_money,
                                order_state=2)
    except:
        rsp_data = copy.copy(settings.ERROR['ERROR'])

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')



@login_required
def order_delete(request):
    ''''''
    rsp_data = copy.copy(settings.ERROR['SUCC'])

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')



@login_required
def state2_save(request):
    '''开证登记保存'''
    rsp_data = copy.copy(settings.ERROR['SUCC'])

    order_id = request.POST['order_id']
    issue_time = request.POST['issue_time']
    issue_money = request.POST['issue_money']
    agency_id = request.POST['agency']
    warning_time = request.POST['warning_time']
    issue_plan_money = request.POST['issue_plan_money']
    issue_file_no = request.POST['issue_file_no']
    agency_money = request.POST['agency_money']
    insurance_money = request.POST['insurance_money']
    total_money = request.POST['total_money']
    ensure_money = request.POST['ensure_money']
    ensure_rate = request.POST['ensure_rate']
    ensure_percent = request.POST['ensure_percent']

    try:
        Step2.objects.filter(car_order_id=order_id).update(
            issue_time=issue_time,issue_money=issue_money,
            agency_id=agency_id,warning_time=warning_time,
            issue_plan_money=issue_plan_money,issue_file_no=issue_file_no,
            agency_money=agency_money,insurance_money=insurance_money,
            total_money=total_money,ensure_money=ensure_money,ensure_rate=ensure_rate,
            ensure_percent=ensure_percent,
        )
        CarOrder.objects.filter(id=order_id).update(state=3)
    except:
        rsp_data = copy.copy(settings.ERROR['ERROR'])

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')

def state3_save(request):
    '''
    预计起运
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    order_id = request.POST['order_id']
    try:

        CarOrder.objects.filter(id=order_id).update(state=4)
    except:
        rsp_data = copy.copy(settings.ERROR['ERROR'])

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')

def state4_save(request):
    '''
    实际起运
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    order_id = request.POST['order_id']
    try:

        CarOrder.objects.filter(id=order_id).update(state=5)
    except:
        rsp_data = copy.copy(settings.ERROR['ERROR'])

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')


def state5_save(request):
    '''
    押汇垫税登记
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    order_id = request.POST['order_id']
    try:

        CarOrder.objects.filter(id=order_id).update(state=6)
    except:
        rsp_data = copy.copy(settings.ERROR['ERROR'])

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')

def state5_save(request):
    '''
    押汇垫税登记
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    order_id = request.POST['order_id']
    try:
        CarOrder.objects.filter(id=order_id).update(state=6)
    except:
        rsp_data = copy.copy(settings.ERROR['ERROR'])

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')


def state6_save(request):
    '''
    到港信息
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    order_id = request.POST['order_id']
    try:

        CarOrder.objects.filter(id=order_id).update(state=7)
    except:
        rsp_data = copy.copy(settings.ERROR['ERROR'])

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')


def state7_save(request):
    '''
    海运费结算
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    order_id = request.POST['order_id']
    try:

        CarOrder.objects.filter(id=order_id).update(state=8)
    except:
        rsp_data = copy.copy(settings.ERROR['ERROR'])

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')


def state8_save(request):
    '''
    拆箱登记
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    order_id = request.POST['order_id']
    try:

        CarOrder.objects.filter(id=order_id).update(state=9)
    except:
        rsp_data = copy.copy(settings.ERROR['ERROR'])

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')