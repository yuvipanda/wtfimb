from django.contrib.gis.db import models

class Stage(models.Model):
    display_name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    mtc_name = models.CharField(max_length=255, null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    is_terminus = models.BooleanField(default=False)
    softlinks = models.ManyToManyField('self', null=True, blank=True)

    objects = models.GeoManager()
    
    class Meta:
        ordering = ['display_name',]
    def __unicode__(self):
        return self.display_name
