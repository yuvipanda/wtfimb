
from south.db import db
from django.db import models
from wtfimb.stages.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Stage.is_terminus'
        db.add_column('stages_stage', 'is_terminus', orm['stages.Stage:is_terminus'])
        ts = [1883,2514,2155,2001,2195,2188,1944,1885,1873,1912,2048,1951,2237,\
        1880,2217,2164,1867,1939,1875,1961,1884,1855,1942,1948,1931]
        for s in Stage.objects.filter(id__in = ts):
            s.is_terminus=True
            s.save()
    
    def backwards(self, orm):
        
        # Deleting field 'Stage.is_terminus'
        db.delete_column('stages_stage', 'is_terminus')
   
    models = {
        'stages.stage': {
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_terminus': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mtc_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'softlinks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['stages.Stage']", 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['stages']
