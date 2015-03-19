#coding:utf-8
import copy
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import (authenticate, login as auth_login, logout as auth_logout)
from django.core.urlresolvers import reverse
from account import settings

@csrf_exempt
def login(request):
    """ 登录 """
    rsp_data = copy.copy(settings.ERROR['SUCC'])

    user = None
    #登录
    if request.method == 'POST':
        if request.POST.get('username', '') and request.POST.get('password', ''):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
            else:
                rsp_data = copy.copy(settings.ERROR['ERROR'])
        else:
            rsp_data = copy.copy(settings.ERROR['PARA_ERR'])


    rsp_data['data'] = {}
    rsp_data['data']['next'] = request.REQUEST.get('next', reverse('home'))
    rsp_data['data']['username'] = request.POST.get('username', '')

    response = TemplateResponse(request,'account/login.html',rsp_data)

    #登录成功，跳转
    if user:
        rsp_data['data']['id'] = user.id
        rsp_data['data']['username'] = user.username
        rsp_data['data']['email'] = user.email
        rsp_data['data']['name'] = user.first_name
        response = HttpResponseRedirect(rsp_data['data']['next'])

    return response

@csrf_exempt
def logout(request):
    '''
    function: 退出登录
    '''
    auth_logout(request)

    return HttpResponseRedirect('/')