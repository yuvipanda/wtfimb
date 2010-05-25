from django.contrib.gis.db import models

from django.contrib.auth.models import User

class Stage(models.Model):
    display_name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    mtc_name = models.CharField(max_length=255, null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    softlinks = models.ManyToManyField('self', null=True, blank=True)

    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.display_name
