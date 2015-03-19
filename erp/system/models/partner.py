#coding:utf8
from django.db import models
from common.models import StateModel,TimeModel,SortModel

class Customer(StateModel,TimeModel):
    '''客户'''
    name = models.CharField(default=u'',max_length=128,verbose_name=u'名称')

    class Meta:
        verbose_name = u'客户'
        verbose_name_plural = u'a-客户'
        app_label = 'system'

class Supplier(StateModel,TimeModel,SortModel):
    '''供货商'''
    name = models.CharField(default=u'',max_length=128,verbose_name=u'名称')
    address = models.CharField(default=u'',max_length=512,verbose_name=u'地址')
    contact = models.CharField(default=u'',max_length=20,verbose_name=u'联系人')
    tel = models.CharField(default=u'',max_length=20,verbose_name=u'电话')

    class Meta:
        verbose_name = u'供货商'
        verbose_name_plural = u'a-供货商'
        app_label = 'system'

class Dealer(StateModel,TimeModel,SortModel):
    '''经销商'''
    name = models.CharField(default=u'',max_length=128,verbose_name=u'名称')
    address = models.CharField(default=u'',max_length=512,verbose_name=u'地址')
    contact = models.CharField(default=u'',max_length=20,verbose_name=u'联系人')
    tel = models.CharField(default=u'',max_length=20,verbose_name=u'电话')

    class Meta:
        verbose_name = u'经销商'
        verbose_name_plural = u'a-经销商'
        app_label = 'system'

class Agency(StateModel,TimeModel,SortModel):
    '''代理公司'''
    name = models.CharField(default=u'',max_length=128,verbose_name=u'名称')
    address = models.CharField(default=u'',max_length=512,verbose_name=u'地址')
    contact = models.CharField(default=u'',max_length=20,verbose_name=u'联系人')
    tel = models.CharField(default=u'',max_length=20,verbose_name=u'电话')

    class Meta:
        verbose_name = u'代理（合作）公司'
        verbose_name_plural = u'b-代理（合作）公司'
        app_label = 'system'

class Shipping(StateModel,TimeModel,SortModel):
    '''船运公司'''
    name = models.CharField(default=u'',max_length=128,verbose_name=u'名称')
    address = models.CharField(default=u'',max_length=512,verbose_name=u'地址')
    contact = models.CharField(default=u'',max_length=20,verbose_name=u'联系人')
    tel = models.CharField(default=u'',max_length=20,verbose_name=u'电话')

    class Meta:
        verbose_name = u'船运公司'
        verbose_name_plural = u'b-船运公司'
        app_label = 'system'

class Logistics(StateModel,TimeModel,SortModel):
    '''物流公司'''
    name = models.CharField(default=u'',max_length=128,verbose_name=u'名称')
    address = models.CharField(default=u'',max_length=512,verbose_name=u'地址')
    contact = models.CharField(default=u'',max_length=20,verbose_name=u'联系人')
    tel = models.CharField(default=u'',max_length=20,verbose_name=u'电话')

    class Meta:
        verbose_name = u'物流公司'
        verbose_name_plural = u'b-物流公司'
        app_label = 'system'


class Port(StateModel,TimeModel,SortModel):
    '''港口'''
    name = models.CharField(default=u'',max_length=128,verbose_name=u'名称')

    class Meta:
        verbose_name = u'港口'
        verbose_name_plural = u'b-港口'
        app_label = 'system'

class Showroom(StateModel,TimeModel,SortModel):
    '''展厅'''
    name = models.CharField(default=u'',max_length=128,verbose_name=u'名称')
    address = models.CharField(default=u'',max_length=512,verbose_name=u'地址')
    contact = models.CharField(default=u'',max_length=20,verbose_name=u'联系人')
    tel = models.CharField(default=u'',max_length=20,verbose_name=u'电话')

    class Meta:
        verbose_name = u'展厅'
        verbose_name_plural = u'c-展厅'
        app_label = 'system'


