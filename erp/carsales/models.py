#coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from common.models import StateModel,TimeModel,NoModel
from system.models import *
from carsales import settings

class CarOrder(NoModel,StateModel,TimeModel):
    '''海外订车 step1'''
    order_no = models.CharField(default=u'',max_length=128,verbose_name=u'订单编号')
    supplier_no = models.CharField(default=u'',max_length=64,verbose_name=u'供货编码')
    supplier = models.ForeignKey(Supplier,verbose_name=u'供货商')
    customer = models.ForeignKey(Customer,verbose_name=u'客户类别')
    #车基本信息
    seat_num = models.SmallIntegerField(default=0,verbose_name=u'座位数量')
    key_num = models.SmallIntegerField(default=0,verbose_name=u'钥匙数量')
    car_type = models.ForeignKey(CarType,verbose_name=u'车型')
    car_type_remark = models.CharField(default=u'',max_length=128,blank=True,verbose_name=u'车型备注（如：颜色）')
    car_type_detail = models.TextField(default=u'',max_length=2000,blank=True,verbose_name=u'车型详配')
    made_time = models.DateField(auto_now_add=True,verbose_name=u'生产日期')
    vin = models.CharField(default=u'',max_length=30,verbose_name=u'VIN')
    engine_no = models.CharField(default=u'',max_length=30,verbose_name=u'发动机号')
    tire_size = models.CharField(default=u'',max_length=128,verbose_name=u'轮胎尺寸')

    #车价
    price = models.IntegerField(default=0,verbose_name=u'车价MSRP')
    #车价币种
    currency = models.ForeignKey(Currency,verbose_name=u'币种')
    rate = models.FloatField(default=1.0,verbose_name=u'当前汇率')

    overseas_deposit = models.CharField(default=u'',max_length=128, verbose_name=u'海外定金（美元or其他）')
    china_deposit = models.CharField(default=u'',max_length=128,verbose_name=u'国内定金（人民币）')
    contract_money = models.CharField(default=u'',max_length=128,verbose_name=u'合同金额（美元or其他）')
    contract_file = models.CharField(default=u'',blank=True,max_length=128, verbose_name=u'合同文件')

    order_registrant = models.ForeignKey(User,related_name='order_registrant',verbose_name=u'订车登记人')

    overseas_deposit_pay = models.IntegerField(default=0,verbose_name=u'海外定金支付')
    china_deposit_pay = models.IntegerField(default=0,verbose_name=u'海外定金支付')
    overseas_deposit_pay_remarks = models.CharField(default=u'',max_length=512,blank=True, verbose_name=u'海外定金支付备注')
    china_deposit_pay_remarks = models.CharField(default=u'',max_length=512,blank=True, verbose_name=u'海外定金支付备注')

    deposit_pay_registrant = models.ForeignKey(User,null=True,blank=True,related_name='deposit_pay_registrant', verbose_name=u'财务登记人')

    order_state = models.SmallIntegerField(default=1, choices=settings.CAR_ORDER_STATE_CHOICES, verbose_name=u'订车状态')
    finance_state = models.SmallIntegerField(default=1,choices=settings.CAR_ORDER_FINANCE_STATE, verbose_name=u'财务状态')

    class Meta:
        verbose_name = u'海外订车'
        verbose_name_plural = u'1-海外订车'
        app_label = 'carsales'

    @property
    def step2(self):
        obj,succ = Step2.objects.get_or_create(car_order_id=self.id)
        return obj

    @property
    def step3(self):
        obj,succ = Step3.objects.get_or_create(car_order_id=self.id)
        return obj

    @property
    def step4(self):
        obj,succ = Step4.objects.get_or_create(car_order_id=self.id)
        return obj

    @property
    def step5(self):
        obj,succ = Step5.objects.get_or_create(car_order_id=self.id)
        return obj


class Step2(StateModel,TimeModel):
    '''开证阶段'''
    car_order = models.ForeignKey(CarOrder,verbose_name=u'汽车订单')
    issue_time = models.DateField(auto_now_add=True,verbose_name=u'开证日期')
    issue_money = models.CharField(default=u'',max_length=256,verbose_name=u'开证金额')
    issue_registrant =  models.ForeignKey(User,null=True,blank=True, related_name='issue_registrant',verbose_name=u'开证登记人')

    agency = models.ForeignKey(Agency,null=True,blank=True,verbose_name=u'代理公司')
    agency_money = models.IntegerField(default=0,verbose_name=u'代理费金额（元）')
    insurance_money = models.IntegerField(default=0,verbose_name=u'保险费金额（元）')
    warning_time = models.DateField(null=True,blank=True,verbose_name=u'预警期')

    budget = models.IntegerField(default=0,verbose_name=u'预算总成本（元）')
#    contract_no = models.CharField(default=u'',null=True,blank=True, max_length=64,verbose_name=u'合同号')

    ensure_money = models.CharField(default=u'',max_length=256,verbose_name=u'保证金金额')
    ensure_percent = models.IntegerField(default=0,verbose_name=u'保证金比例')
    ensure_rate = models.FloatField(default=0,verbose_name=u'保证金协议汇率')

    #财务
    issue_pay_money = models.IntegerField(default=0,verbose_name=u'开证费用')
    issue_pay_obj = models.ForeignKey(Customer,null=True,blank=True,verbose_name=u'支付对象')
    issue_pay_time = models.DateField(auto_now_add=True,verbose_name=u'支付时间')
    issue_pay_registrant = models.ForeignKey(User,null=True,blank=True,related_name='issue_pay_registrant', verbose_name=u'财务登记人')

    class Meta:
        verbose_name = u'开证阶段'
        verbose_name_plural = u'2-开证阶段'
#        app_label = 'carsales'

class Step3(StateModel,TimeModel):
    '''起运阶段'''
    car_order = models.ForeignKey(CarOrder,verbose_name=u'汽车订单')
    port_plan_start = models.ForeignKey(Port,null=True,blank=True,related_name='port_plan_start', verbose_name=u'预计起运港')
    port_plan_end = models.ForeignKey(Port,null=True,blank=True,related_name='port_plan_end', verbose_name=u'预计目标港')
    time_plan_start = models.DateField(null=True,blank=True,verbose_name=u'预计起运时间')
    time_plan_end = models.DateField(null=True,blank=True,verbose_name=u'预计到港时间')
    shipping_plan = models.ForeignKey(Agency,null=True,blank=True,related_name='shipping_plan',verbose_name=u'承运公司')
    plan_registrant = models.ForeignKey(User,null=True,blank=True,related_name='plan_registrant',verbose_name=u'预计起运登记人')

    port_real_start = models.ForeignKey(Port,null=True,blank=True,related_name='port_real_start',verbose_name=u'实际起运港')
    port_real_end = models.ForeignKey(Port,null=True,blank=True,related_name='port_real_end',verbose_name=u'实际目标港')
    time_real_start = models.DateField(null=True,blank=True,verbose_name=u'实际起运时间')
    time_real_end = models.DateField(null=True,blank=True,verbose_name=u'实际到港时间')
    lading_no = models.CharField(default=u'',blank=True,max_length=64,verbose_name=u'提单号码')
    shipping_real = models.ForeignKey(Shipping,null=True,blank=True,related_name='shipping_real',verbose_name=u'承运公司')
    real_registrant = models.ForeignKey(User,null=True,blank=True,related_name='real_registrant',verbose_name=u'实际起运登记人')

    bill_time = models.DateField(null=True,blank=True,verbose_name=u'押汇登记时间')
    bill_money = models.CharField(default=u'',max_length=256,verbose_name=u'押汇金额')
    bill_agency = models.ForeignKey(Agency,null=True,blank=True,verbose_name=u'押汇代理公司')
    bill_file = models.CharField(default=u'',max_length=128,verbose_name=u'押汇协议')
    bill_warning_time = models.DateField(null=True,blank=True,verbose_name=u'押汇预警期')
    bill_registrant = models.ForeignKey(User,null=True,blank=True,related_name='bill_registrant',verbose_name=u'押汇登记人')

    bill_pay_money = models.IntegerField(default=0,verbose_name=u'押汇费用')
    bill_pay_obj = models.ForeignKey(Customer,null=True,blank=True,verbose_name=u'支付对象')
    bill_pay_time = models.DateField(null=True,blank=True,verbose_name=u'支付时间')
    bill_pay_registrant = models.ForeignKey(User,null=True,blank=True,related_name='bill_pay_registrant',verbose_name=u'财务登记人')

    class Meta:
            verbose_name = u'起运阶段'
            verbose_name_plural = u'3-起运阶段'
            app_label = 'carsales'

class Step4(StateModel,TimeModel):
    '''到港阶段'''
    car_order = models.ForeignKey(CarOrder,verbose_name=u'订单')
    port_start = models.ForeignKey(Port,null=True,blank=True,related_name='port_start',verbose_name=u'起运港')
    port_end = models.ForeignKey(Port,null=True,blank=True,related_name='port_end',verbose_name=u'目标港')
    port_registrant = models.ForeignKey(User,null=True,blank=True,related_name='port_registrant',verbose_name=u'到港登记人')
    port_time = models.DateField(null=True,blank=True,verbose_name=u'到港时间')
    shipping = models.ForeignKey(Shipping,null=True,blank=True,related_name='shipping', verbose_name=u'船运公司')

    #二次转港
    port_second_start = models.ForeignKey(Port,related_name='port_second_start',verbose_name=u'二次起运港')
    port_second_end = models.ForeignKey(Port,related_name='port_second_end',verbose_name=u'二次目标港')
    port_second_time = models.DateField(null=True,blank=True,verbose_name=u'转港时间')
    port_second_registrant = models.ForeignKey(User,related_name='port_second_registrant',verbose_name=u'二次登记人')
    shipping_second = models.ForeignKey(Shipping,related_name='shipping_second',verbose_name=u'二次船运公司')

    #海运费
    shipping_obj = models.ForeignKey(Shipping,null=True,blank=True,related_name='shipping_obj',verbose_name=u'付款对象')
    shipping_money = models.CharField(default=u'',max_length=128,verbose_name=u'海运费')
    shipping_money_registrant = models.ForeignKey(User,null=True,blank=True,related_name='shipping_money_registrant',
                                                  verbose_name=u'海运费')
    shipping_second_money = models.CharField(default=u'',max_length=128,verbose_name=u'转港费用')

    #财务登记
    shipping_pay_money = models.IntegerField(default=0,verbose_name=u'海运支付金额（财务）')
    shipping_pay_time = models.DateField(null=True,blank=True,verbose_name=u'海运支付时间（财务）')
    shipping_pay_registrant = models.ForeignKey(User,null=True,blank=True,
                                related_name='shipping_pay_registrant',verbose_name=u'海运费登记人')
    #转港财务登记
    shipping_second_pay_money = models.IntegerField(default=0,verbose_name=u'转港支付金额（财务）')
    shipping_second_pay_time = models.DateField(null=True,blank=True,verbose_name=u'海运支付时间（财务）')
    shipping_second_pay_registrant = models.ForeignKey(User,null=True,blank=True,
                                related_name='shipping_second_pay_registrant',verbose_name=u'转港海运费登记人')

    class Meta:
        verbose_name = u'到港阶段'
        verbose_name_plural = u'4-到港阶段'
        app_label = 'carsales'

class Step5(StateModel,TimeModel):
    '''
    报关阶段
    '''
    car_order = models.ForeignKey(CarOrder,verbose_name=u'订单')
    devanning_time = models.DateField(auto_now_add=True,verbose_name=u'拆箱时间')
    devanning_registrant = models.ForeignKey(User,null=True,blank=True,related_name='devanning_registrant',
                                            verbose_name=u'拆箱登记人')

    show_time = models.DateField(auto_now_add=True,verbose_name=u'保税展示起始时间')
    show_room = models.ForeignKey(Showroom,null=True,blank=True,verbose_name=u'展厅')
    show_registrant = models.ForeignKey(User,null=True,blank=True,related_name='show_registrant',
                                        verbose_name=u'保税展示登记人')

    # OBD
    obd_time = models.DateField(auto_now_add=True,verbose_name=u'OBD时间')
    obd_no = models.CharField(default=u'',blank=True,max_length=30,verbose_name=u'OBD设备号码')
    obd_registrant = models.ForeignKey(User,null=True,blank=True,related_name='obd_registrant',
                                   verbose_name=u'OBD登记人')

    sn_time = models.DateField(auto_now=True,verbose_name=u'商检报关时间')
    sn_remark = models.TextField(default=u'',verbose_name=u'商检报关备注')
    sn_registrant = models.ForeignKey(User,null=True,blank=True,related_name='sn_registrant',verbose_name=u'商检登记人')

    out_tax_money = models.IntegerField(default=0,verbose_name=u'出税金额')
    out_tax_time = models.DateField(auto_now_add=True,verbose_name=u'出税时间')
    out_tax_registrant = models.ForeignKey(User,null=True,blank=True,related_name='out_tax_registrant',verbose_name=u'商检登记人')

    mat_tax_agency = models.ForeignKey(Agency,null=True,blank=True,related_name='mat_tax_agency',verbose_name=u'垫税代理公司')
    mat_tax_money = models.IntegerField(default=0,verbose_name=u'垫税金额')

    real_tax_money = models.IntegerField(default=0,verbose_name=u'税金付讫实际金额')
    real_tax_obj = models.ForeignKey(Agency,null=True,blank=True,verbose_name=u'支付对象')
    real_tax_time = models.DateField(null=True,verbose_name=u'支付时间')
    real_tax_remark = models.TextField(default=u'',verbose_name=u'税金备注')
    real_tax_registrant = models.ForeignKey(User,null=True,blank=True,related_name='real_tax_registrant',verbose_name=u'税金登记人')

    customer_tax_money = models.IntegerField(default=0,verbose_name=u'客户预付定金')
    customer_tax_time = models.DateField(auto_now_add=True,null=True,blank=True,verbose_name=u'客户预付时间')
    customer_tax_registrant = models.ForeignKey(User,null=True,blank=True,related_name='customer_tax_registrant',
                                                verbose_name=u'客户预付登记人')

    pdi_time = models.DateField(auto_now_add=True,verbose_name=u'PDI检测时间')
    pdi_agency = models.ForeignKey(Agency,null=True,blank=True,related_name='pdi_agency', verbose_name=u'PDI检测公司')
    pdi_remark = models.TextField(default=u'',blank=True,verbose_name=u'PDI整改备注')
    pdi_registrant = models.ForeignKey(User,null=True,blank=True,related_name='pdi_registrant',verbose_name=u'PDI登记人')

    end_tax_time = models.DateField(auto_now_add=True,verbose_name=u'报关完成时间')
    end_tax_remark = models.TextField(default=u'',blank=True,verbose_name=u'报关完成问题备注')
    end_tax_registrant = models.ForeignKey(User,null=True,blank=True,related_name='end_tax_registrant',
        verbose_name=u'报关完成登记人')

    end_money = models.IntegerField(default=0,blank=True,verbose_name=u'整车尾款')
    end_money_registrant =  models.ForeignKey(User,null=True,blank=True,related_name='end_money_registrant',
        verbose_name=u'整车尾款登记人')

    end_real_pay_money = models.IntegerField(default=0,blank=True,verbose_name=u'整车尾款实收')
    end_real_pay_time = models.DateField(auto_now_add=True,verbose_name=u'整车尾款支付时间')
    end_need_pay_money = models.IntegerField(default=0,blank=True,verbose_name=u'整车尾款待收金额')
    end_pay_registrant = models.ForeignKey(User,null=True,blank=True,related_name='end_pay_registrant',
        verbose_name=u'整车尾款登记人(财务)')

    release_time = models.DateField(auto_now_add=True,verbose_name=u'进口商放行时间')
    release_remark = models.TextField(default=u'',blank=True,verbose_name=u'进口商放行备注')
    release_registrant = models.ForeignKey(User,null=True,blank=True,related_name='release_registrant',
        verbose_name=u'进口商放行登记人')

    class Meta:
        verbose_name = u'报关阶段'
        verbose_name_plural = u'5-报关阶段'
        app_label = 'carsales'

