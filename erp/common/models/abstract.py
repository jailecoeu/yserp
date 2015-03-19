#coding: utf-8

from django.db import models

STATE_CHOICES = (
    ( 0, u'正常' ),
    ( 1, u'临时记录'),
    ( 9, u'删除' ),
)

class TimeModel(models.Model):
    '''
    class: 包含创建和修改时间的基础类
    '''
    
    create_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=u'创建时间')
    modify_time = models.DateTimeField(auto_now=True, db_index=True, verbose_name=u'更新时间')
    
    class Meta:
        abstract = True

class NoModel(models.Model):
    '''
    class: 包含唯一编号的基础类
    '''
    no = models.CharField(max_length=128, unique=True, verbose_name=u'编号')
    
    class Meta:
        abstract = True

class StateModel(models.Model):
    '''
    class: 包含记录状态的基础类0--正常 9--删除
    '''
    state = models.IntegerField(choices=STATE_CHOICES, default=0, db_index=True, verbose_name=u'记录状态')

    class Meta:
        abstract = True
    
    def logic_delete(self):
        self.state = 9
        self.save()


class SortModel(models.Model):
    '''
    class: 包含排序的基础类
    '''
    sort = models.IntegerField(default=0, verbose_name=u'排序',help_text=u'越小越靠前')

    class Meta:
        abstract = True