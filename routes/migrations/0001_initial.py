
from south.db import db
from django.db import models
from wtfimb.routes.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'RouteStage'
        db.create_table('routes_routestage', (
            ('id', orm['routes.RouteStage:id']),
            ('route', orm['routes.RouteStage:route']),
            ('stage', orm['routes.RouteStage:stage']),
            ('sequence', orm['routes.RouteStage:sequence']),
        ))
        db.send_create_signal('routes', ['RouteStage'])
        
        # Adding model 'Route'
        db.create_table('routes_route', (
            ('id', orm['routes.Route:id']),
            ('display_name', orm['routes.Route:display_name']),
            ('mtc_name', orm['routes.Route:mtc_name']),
            ('types', orm['routes.Route:types']),
            ('start', orm['routes.Route:start']),
            ('end', orm['routes.Route:end']),
            ('time', orm['routes.Route:time']),
            ('fare', orm['routes.Route:fare']),
        ))
        db.send_create_signal('routes', ['Route'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'RouteStage'
        db.delete_table('routes_routestage')
        
        # Deleting model 'Route'
        db.delete_table('routes_route')
        
    
    
    models = {
        'routes.route': {
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'end': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'end'", 'to': "orm['stages.Stage']"}),
            'fare': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtc_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'stages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['stages.Stage']"}),
            'start': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'start'", 'to': "orm['stages.Stage']"}),
            'time': ('django.db.models.fields.FloatField', [], {}),
            'types': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'routes.routestage': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['routes.Route']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stages.Stage']"})
        },
        'stages.stage': {
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mtc_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['routes']
