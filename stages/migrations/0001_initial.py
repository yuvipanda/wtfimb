# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Stage'
        db.create_table('stages_stage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('mtc_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('importance', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('is_terminus', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('stages', ['Stage'])


    def backwards(self, orm):
        
        # Deleting model 'Stage'
        db.delete_table('stages_stage')


    models = {
        'stages.stage': {
            'Meta': {'object_name': 'Stage'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_terminus': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mtc_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stages']
