# coding: utf-8

import json
from django.utils.http import urlquote
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from account import settings

def login_required(view_func):
    ''''''
    def _check_login(request, *args, **kwargs):
        
        if request.user.is_authenticated():
            return view_func(request, *args, **kwargs)
        else:
            if request.is_ajax():
                response = HttpResponse(json.dumps(settings.ERROR['NOT_LOGIN_ERR']), 
                                    mimetype = 'application/json')
            else:
                response =  HttpResponseRedirect('%s?next=%s' % \
                                    (settings.LOGIN_URL, urlquote(request.get_full_path())))
            return response
            
    return _check_login


def unlogin_required(view_func):
    """ 要求未登录 """
    def _check_login(request, *args, **kwargs):
        
        if request.user.is_authenticated():
            if request.is_ajax():
                return HttpResponse(json.dumps(settings.ERROR['ERROR']), 
                                    mimetype = 'application/json')
            else:
                return HttpResponseRedirect(reverse('home'))
        return view_func(request, *args, **kwargs)
    return _check_login
