# coding: utf-8
#__author__ = 'Administrator'
#__create__ = '13-9-11'
from django.conf import settings

ERROR = {}
ERROR.update(settings.ERROR)


CAR_ORDER_STATE_CHOICES = (
    (0,u'---'),
    (1,u'海外订车'),
    (2,u'开证阶段-开证登记'),
    (3,u'开证阶段-保证金登记'),
    (4,u'起运阶段-预计起运'),
    (5,u'起运阶段-实际起运'),
    (6,u'起运阶段-押汇垫税登记'),
    (7,u'到港阶段-到港信息'),
    (8,u'到港阶段-海运费结算'),
    (9,u'报关阶段-拆箱登记'),
    (10,u'报关阶段-保税展示登记'),

)

CAR_ORDER_FINANCE_STATE = (
    (0,u'---'),
    (1,u'海外订车登记'),
    (2,u'开证阶段登记'),
)