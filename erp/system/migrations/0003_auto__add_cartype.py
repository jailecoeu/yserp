# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CarType'
        db.create_table('system_cartype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('brand', self.gf('django.db.models.fields.CharField')(default=u'', max_length=256)),
            ('series', self.gf('django.db.models.fields.CharField')(default=u'', max_length=256)),
            ('series_no', self.gf('django.db.models.fields.CharField')(default=u'', max_length=256)),
            ('years', self.gf('django.db.models.fields.CharField')(default=u'', max_length=256)),
            ('conf', self.gf('django.db.models.fields.CharField')(default=u'', max_length=256)),
            ('version', self.gf('django.db.models.fields.CharField')(default=u'', max_length=256)),
        ))
        db.send_create_signal('system', ['CarType'])


    def backwards(self, orm):
        # Deleting model 'CarType'
        db.delete_table('system_cartype')


    models = {
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
        'system.dealer': {
            'Meta': {'object_name': 'Dealer'},
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
        'system.kwdict': {
            'Meta': {'ordering': "('code',)", 'unique_together': "(('value', 'code'),)", 'object_name': 'KwDict'},
            'code': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'value': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'system.logistics': {
            'Meta': {'object_name': 'Logistics'},
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

    complete_apps = ['system']