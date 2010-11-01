# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Route.city'
        db.add_column('routes_route', 'city', self.gf('django.db.models.fields.CharField')(default='chennai', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Route.city'
        db.delete_column('routes_route', 'city')


    models = {
        'routes.route': {
            'Meta': {'object_name': 'Route'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'end': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'end_for_routes'", 'to': "orm['stages.Stage']"}),
            'fare': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtc_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '64', 'db_index': 'True'}),
            'stages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['stages.Stage']", 'through': "orm['routes.RouteStage']", 'symmetrical': 'False'}),
            'start': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'start_for_routes'", 'to': "orm['stages.Stage']"}),
            'time': ('django.db.models.fields.FloatField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'B'", 'max_length': '1'}),
            'types': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'routes.routestage': {
            'Meta': {'object_name': 'RouteStage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['routes.Route']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'routelinks'", 'to': "orm['stages.Stage']"})
        },
        'stages.stage': {
            'Meta': {'object_name': 'Stage'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_terminus': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mtc_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'softlinks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['stages.Stage']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['routes']
