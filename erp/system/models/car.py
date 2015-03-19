#coding:utf8
from django.db import models
from common.models import StateModel,TimeModel,SortModel

class CarType(StateModel,TimeModel,SortModel):
    '''车型'''
    brand = models.CharField(default=u'',max_length=256,verbose_name=u'品牌')
    series = models.CharField(default=u'',max_length=256,verbose_name=u'车系')
    series_no = models.CharField(default=u'',max_length=256,verbose_name=u'车型')
    years = models.CharField(default=u'',max_length=256,verbose_name=u'年款')
    conf = models.CharField(default=u'',max_length=256,verbose_name=u'配置')
    version = models.CharField(default=u'',max_length=256,verbose_name=u'版本')

    class Meta:
        verbose_name = u'车型'
        verbose_name_plural = u'0-车型'
        app_label = 'system'

    def __unicode__(self):
        return u'%s/%s/%s/%s/%s/%s' % (self.brand,self.series,self.series_no,self.years,self.conf,self.version)