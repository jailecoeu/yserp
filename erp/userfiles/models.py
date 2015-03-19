#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from common.models.abstract import StateModel,TimeModel
from userfiles import settings
from django.core.files.storage import default_storage

class UFile(StateModel,TimeModel):
    '''
    用户文件存储
    '''
    user = models.ForeignKey(User,verbose_name=u'用户')
    fpath = models.CharField(default=u'',max_length=128, blank=True, verbose_name=u'文件地址')
    desc = models.CharField(default=u'',blank=True,max_length=1000, verbose_name=u'图片描述')
    xsize = models.SmallIntegerField(default=0,verbose_name=u'宽')
    ysize = models.SmallIntegerField(default=0,verbose_name=u'高')
    msize = models.IntegerField(default=0,verbose_name=u'文件大小')
    ftype = models.SmallIntegerField(default=0,choices=settings.UFILE_FTYPE_CHOICES,verbose_name=u'所属类别')

    class Meta:
        verbose_name = u'用户文件'
        verbose_name_plural = u'用户文件'
        app_label = 'userfiles'
        db_table = 'image'

    def __unicode__(self):
        return self.fpath
    
    @property
    def file_url(self):
        """ 文件url地址 """
        return default_storage.url(self.fpath)