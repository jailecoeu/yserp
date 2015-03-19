# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Step2.issue_money'
        db.alter_column('carsales_step2', 'issue_money', self.gf('django.db.models.fields.CharField')(max_length=256))
        # Adding field 'Step5.car_order'
        db.add_column('carsales_step5', 'car_order',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['carsales.CarOrder']),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Step2.issue_money'
        db.alter_column('carsales_step2', 'issue_money', self.gf('django.db.models.fields.IntegerField')())
        # Deleting field 'Step5.car_order'
        db.delete_column('carsales_step5', 'car_order_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'carsales.carorder': {
            'Meta': {'object_name': 'CarOrder'},
            'car_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.CarType']"}),
            'car_type_detail': ('django.db.models.fields.TextField', [], {'default': "u''", 'max_length': '2000', 'blank': 'True'}),
            'car_type_remark': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'china_deposit': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'china_deposit_pay': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'china_deposit_pay_remarks': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512', 'blank': 'True'}),
            'contract_file': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'contract_money': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Currency']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Customer']"}),
            'deposit_pay_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'deposit_pay_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'engine_no': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '30'}),
            'finance_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_num': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'made_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'no': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'order_no': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'order_registrant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'order_registrant'", 'to': "orm['auth.User']"}),
            'order_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'overseas_deposit': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'overseas_deposit_pay': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'overseas_deposit_pay_remarks': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rate': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'seat_num': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Supplier']"}),
            'supplier_no': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64'}),
            'tire_size': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'vin': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '30'})
        },
        'carsales.step2': {
            'Meta': {'object_name': 'Step2'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Agency']", 'null': 'True', 'blank': 'True'}),
            'agency_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'budget': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'car_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['carsales.CarOrder']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'ensure_money': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256'}),
            'ensure_percent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ensure_rate': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'issue_money': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256'}),
            'issue_pay_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'issue_pay_obj': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Customer']", 'null': 'True', 'blank': 'True'}),
            'issue_pay_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'issue_pay_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'issue_pay_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'issue_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'issue_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'issue_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'warning_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'carsales.step3': {
            'Meta': {'object_name': 'Step3'},
            'bill_agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Agency']", 'null': 'True', 'blank': 'True'}),
            'bill_file': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'bill_money': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256'}),
            'bill_pay_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bill_pay_obj': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Customer']", 'null': 'True', 'blank': 'True'}),
            'bill_pay_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bill_pay_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'bill_pay_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'bill_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bill_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'bill_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'bill_warning_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'car_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['carsales.CarOrder']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lading_no': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'plan_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'plan_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'port_plan_end': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'port_plan_end'", 'null': 'True', 'to': "orm['system.Port']"}),
            'port_plan_start': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'port_plan_start'", 'null': 'True', 'to': "orm['system.Port']"}),
            'port_real_end': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'port_real_end'", 'null': 'True', 'to': "orm['system.Port']"}),
            'port_real_start': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'port_real_start'", 'null': 'True', 'to': "orm['system.Port']"}),
            'real_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'real_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'shipping_plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'shipping_plan'", 'null': 'True', 'to': "orm['system.Agency']"}),
            'shipping_real': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'shipping_real'", 'null': 'True', 'to': "orm['system.Shipping']"}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'time_plan_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_plan_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_real_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_real_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'carsales.step4': {
            'Meta': {'object_name': 'Step4'},
            'car_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['carsales.CarOrder']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'port_end': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'port_end'", 'null': 'True', 'to': "orm['system.Port']"}),
            'port_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'port_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'port_second_end': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'port_second_end'", 'to': "orm['system.Port']"}),
            'port_second_registrant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'port_second_registrant'", 'to': "orm['auth.User']"}),
            'port_second_start': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'port_second_start'", 'to': "orm['system.Port']"}),
            'port_second_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'port_start': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'port_start'", 'null': 'True', 'to': "orm['system.Port']"}),
            'port_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'shipping': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'shipping'", 'null': 'True', 'to': "orm['system.Shipping']"}),
            'shipping_money': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'shipping_money_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'shipping_money_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'shipping_obj': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'shipping_obj'", 'null': 'True', 'to': "orm['system.Shipping']"}),
            'shipping_pay_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'shipping_pay_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'shipping_pay_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'shipping_pay_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_second': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shipping_second'", 'to': "orm['system.Shipping']"}),
            'shipping_second_money': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'shipping_second_pay_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'shipping_second_pay_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'shipping_second_pay_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'shipping_second_pay_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        'carsales.step5': {
            'Meta': {'object_name': 'Step5'},
            'car_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['carsales.CarOrder']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'customer_tax_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'customer_tax_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customer_tax_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'customer_tax_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'devanning_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'devanning_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'devanning_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_money': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'end_money_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'end_money_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'end_need_pay_money': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'end_pay_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'end_pay_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'end_real_pay_money': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'end_real_pay_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_tax_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'end_tax_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'end_tax_remark': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'end_tax_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mat_tax_agency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mat_tax_agency'", 'null': 'True', 'to': "orm['system.Agency']"}),
            'mat_tax_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'obd_no': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '30', 'blank': 'True'}),
            'obd_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'obd_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'obd_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'out_tax_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'out_tax_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'out_tax_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'out_tax_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'pdi_agency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pdi_agency'", 'null': 'True', 'to': "orm['system.Agency']"}),
            'pdi_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pdi_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'pdi_remark': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'pdi_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'real_tax_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'real_tax_obj': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Agency']", 'null': 'True', 'blank': 'True'}),
            'real_tax_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'real_tax_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'real_tax_remark': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'real_tax_time': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'release_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'release_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'release_remark': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'release_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'show_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'show_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'show_room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Showroom']", 'null': 'True', 'blank': 'True'}),
            'show_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sn_registrant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sn_registrant'", 'null': 'True', 'to': "orm['auth.User']"}),
            'sn_remark': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'sn_time': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'system.agency': {
            'Meta': {'object_name': 'Agency'},
            'address': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512'}),
            'contact': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20'})
        },
        'system.cartype': {
            'Meta': {'object_name': 'CarType'},
            'brand': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256'}),
            'conf': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256'}),
            'series_no': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256'}),
            'years': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '256'})
        },
        'system.currency': {
            'Meta': {'object_name': 'Currency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'rate': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        'system.customer': {
            'Meta': {'object_name': 'Customer'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        'system.port': {
            'Meta': {'object_name': 'Port'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        'system.shipping': {
            'Meta': {'object_name': 'Shipping'},
            'address': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512'}),
            'contact': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20'})
        },
        'system.showroom': {
            'Meta': {'object_name': 'Showroom'},
            'address': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512'}),
            'contact': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20'})
        },
        'system.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'address': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '512'}),
            'contact': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20'})
        }
    }

    complete_apps = ['carsales']