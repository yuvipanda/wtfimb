
from south.db import db
from django.db import models
from wtfimb.routes.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Route.slug'
        db.add_column('routes_route', 'slug', orm['routes.route:slug'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Route.slug'
        db.delete_column('routes_route', 'slug')
        
    
    
    models = {
        'routes.route': {
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'end': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'end_for_routes'", 'to': "orm['stages.Stage']"}),
            'fare': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtc_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '64', 'db_index': 'True'}),
            'stages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['stages.Stage']"}),
            'start': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'start_for_routes'", 'to': "orm['stages.Stage']"}),
            'time': ('django.db.models.fields.FloatField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'B'", 'max_length': '1'}),
            'types': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'routes.routestage': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['routes.Route']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'routelinks'", 'to': "orm['stages.Stage']"})
        },
        'stages.stage': {
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mtc_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'softlinks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['stages.Stage']"})
        }
    }
    
    complete_apps = ['routes']
