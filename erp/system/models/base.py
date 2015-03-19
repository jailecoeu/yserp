#coding:utf8
from django.db import models
from common.models import StateModel,SortModel

class KwDict(StateModel,SortModel):
    '''字典'''
    name = models.CharField(default=u'',max_length=128,verbose_name=u'名称')
    value = models.SmallIntegerField(default=0,verbose_name=u'值')
    code = models.CharField(default=u'',max_length=50, verbose_name=u'编号')

    class Meta:
        verbose_name = u'字典'
        verbose_name_plural = u'0-字典'
        app_label = 'system'
        unique_together = (('value','code'),)
        ordering = ('code',)

class Currency(StateModel,SortModel):
    '''货币'''
    name = models.CharField(default=u'',max_length=128,verbose_name=u'名称')
    rate = models.FloatField(default=1.0, verbose_name=u'默认汇率',help_text=u'转换成人民币的倍数')

    class Meta:
        verbose_name = u'币种'
        verbose_name_plural = u'0-币种'
        app_label = 'system'