# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'KwDict'
        db.create_table('system_kwdict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128)),
            ('value', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('code', self.gf('django.db.models.fields.CharField')(default=u'', max_length=50)),
        ))
        db.send_create_signal('system', ['KwDict'])

        # Adding unique constraint on 'KwDict', fields ['value', 'code']
        db.create_unique('system_kwdict', ['value', 'code'])

        # Adding model 'Supplier'
        db.create_table('system_supplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(default=u'', max_length=512)),
            ('contact', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
            ('tel', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
        ))
        db.send_create_signal('system', ['Supplier'])

        # Adding model 'Dealer'
        db.create_table('system_dealer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(default=u'', max_length=512)),
            ('contact', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
            ('tel', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
        ))
        db.send_create_signal('system', ['Dealer'])

        # Adding model 'Agency'
        db.create_table('system_agency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(default=u'', max_length=512)),
            ('contact', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
            ('tel', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
        ))
        db.send_create_signal('system', ['Agency'])

        # Adding model 'Shipping'
        db.create_table('system_shipping', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(default=u'', max_length=512)),
            ('contact', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
            ('tel', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
        ))
        db.send_create_signal('system', ['Shipping'])

        # Adding model 'Logistics'
        db.create_table('system_logistics', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(default=u'', max_length=512)),
            ('contact', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
            ('tel', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
        ))
        db.send_create_signal('system', ['Logistics'])

        # Adding model 'Showroom'
        db.create_table('system_showroom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(default=u'', max_length=512)),
            ('contact', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
            ('tel', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20)),
        ))
        db.send_create_signal('system', ['Showroom'])


    def backwards(self, orm):
        # Removing unique constraint on 'KwDict', fields ['value', 'code']
        db.delete_unique('system_kwdict', ['value', 'code'])

        # Deleting model 'KwDict'
        db.delete_table('system_kwdict')

        # Deleting model 'Supplier'
        db.delete_table('system_supplier')

        # Deleting model 'Dealer'
        db.delete_table('system_dealer')

        # Deleting model 'Agency'
        db.delete_table('system_agency')

        # Deleting model 'Shipping'
        db.delete_table('system_shipping')

        # Deleting model 'Logistics'
        db.delete_table('system_logistics')

        # Deleting model 'Showroom'
        db.delete_table('system_showroom')


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