# coding: utf-8
#__author__ = 'chang'
#__create__ = '14-11-6'

upload_params = [
    {'name':'type' ,    'must':True,    'method':'POST',   'regex': '^(|default|img|swf|user_banner)$','desc': u'上传类型'},
    {'name': 'file',    'must': True,   'method': 'FILES', 'regex': '.*',       'desc': u'文件'},
]

upload_swf_params = [
    {'name': 'uid',     'must': True,   'method': 'POST', 'regex': '^\d+$', 'desc': u'用户ID'},
    {'name': 'uname',   'must': True,   'method': 'POST', 'regex': '^.{0,30}$', 'desc': u'用户名'},
    {'name': 'rnd',     'must': True,   'method': 'POST', 'regex': '.*', 'desc': u'验签'},
    {'name': 'type' ,    'must':True,    'method':'POST',   'regex': '^(|default|img|swf|user_banner|avatar)$','desc': u'上传类型'},
    {'name': 'file',    'must': True,   'method': 'FILES', 'regex': '.*',       'desc': u'文件'},
]