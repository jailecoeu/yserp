# coding: utf-8
#__author__ = 'Administrator'
#__create__ = '13-9-11'
from django.conf import settings

ERROR = {}
ERROR.update(settings.ERROR)

LOGIN_URL = getattr(settings, 'LOGIN_URL', '/account/login/')