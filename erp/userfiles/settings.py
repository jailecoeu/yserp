# coding: utf-8
#__author__ = 'chang'
#__create__ = '14-11-6'
from django.conf import settings

MEDIA_URL = settings.MEDIA_URL
MEDIA_ROOT = settings.MEDIA_ROOT

STATIC_URL = settings.STATIC_URL

ERROR ={
    'UPLOAD_RULE_ERROR': {'code': '60001', 'msg': u'上传规则错误'},
    'FILE_EXT_ERROR': {'code': '60002', 'msg': u'文件格式错误'},
    'FILE_MAX_SIZE_ERROR': {'code': '60003', 'msg': u'文件大小超过限制'},
    'FILE_XYSIZE_ERROR': {'code': '60004', 'msg': u'图片尺寸规格错误'},
    'FILE_TOTAL_COUNT_ERROR': {'code': '60005', 'msg': u'文件总数超出限制'},
    'FILE_TOTAL_SIZE_ERROR': {'code': '60006', 'msg': u'文件存储超出限制'},
    'FILE_SAVE_ERROR': {'code': '60007', 'msg': u'文件存储失败'},
}
ERROR.update(settings.ERROR)

UFILE_FTYPE_COMMON_FILE = 0
UFILE_FTYPE_COMMON_PIC = 1
UFILE_FTYPE_SWF_FILE = 2
UFILE_FTYPE_BANNER_PIC = 3
UFILE_FTYPE_AVATAR = 4
UFILE_FTYPE_COVER_PIC = 5

UFILE_FTYPE_CHOICES = (
    (UFILE_FTYPE_COMMON_FILE,u'通用文件'),
    (UFILE_FTYPE_COMMON_PIC,u'通用图片'),
    (UFILE_FTYPE_SWF_FILE,u'swf文件'),
    (UFILE_FTYPE_BANNER_PIC,u'用户主页封面图'),
    (UFILE_FTYPE_AVATAR,u'用户头像'),
)


ITEM_TYPE_CHOICES =  (
    (0,u'通用附件'),
    (1,u'图片'),
    (2,u'户型图'),
    (3,u'设计效果图'),
)


#***********************************************************************#
#                         文件上传规则说明                              #
# default|img ...: 上传规则名称
# type :           上传规则 代号 需与  上边 UFILE_FTYPE_CHOICES 对应
# ext  :           上传文件格式  [] 空代表不检查
# file_size_max :  文件上传大小限制
# folder     :     文件保存文件夹名称，保存优先： 规则设定 > 客户端post > 时间20150101
# file_name  :     文件保存名， 保存优先 ： 规则设定 > 客户端post > uuid 重命名
# xsize      :     图片文件上传最小宽度限制 ，eg:200
# ysize      :     图片文件上传最小高度限制 ，eg:300
# total_count:     该类文件上传个数限制 ,     eg: 2
# total_size :     该类文件上传总大小限制,    eg:2*1024*1024
# unique     :     是否唯一，默认 False
#***********************************************************************#

USER_FILE_SAVE_RULE = {
    'default':{'type':0,'ext':[],'file_size_max':2*1024*1024,'folder':'',
           'total_count':0,'total_size':0},
                       
    'img':{'type':1,'ext':['JPG','JPEG','PNG'],'file_size_max':2*1024*1024,'folder':'',
           'xsize':0,'ysize':0,
           'total_count':0,'total_size':0},
                       
    'swf':{'type':2,'ext':['SWF'],'file_size_max':2*1024*1024,'folder':'',
           'total_count':0,'total_size':0},
                       
    'user_banner':{'type':3,'ext':['JPG','JPEG','PNG'],'file_size_max':3*1024*1024,'folder':'banner',
                   'file_name':'',
           'total_count':1,'total_size':0,'unique':True},
                       
    'avatar':{'type':4,'ext':['JPG','JPEG','PNG'],'file_size_max':2*1024*1024,'folder':'avatar',
              'file_name':'',
              'total_count':1,'total_size':0,'unique':True},
    'ueditor_image':{
        'type':5,'ext':['JPG','JPEG','PNG'],'file_size_max':2*1024*1024,'folder':'ueditor',
        'file_name':'',
        'total_count':1,'total_size':0,'save_db':False
    }
}


UEditorUploadSettings={
    #上传图片配置项
    "imageActionName": "uploadimage", #执行上传图片的action名称
    "imageMaxSize": 2*1024*1024, #上传大小限制，单位B,10M
    "imageFieldName": "upfile", #* 提交的图片表单名称 */
    "imageUrlPrefix":"",
    "imagePathFormat":"",
    "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], #上传图片格式显示
}
