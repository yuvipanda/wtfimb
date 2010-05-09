from django.contrib.gis.db import models

from django.contrib.auth.models import User

class Stage(models.Model):
    display_name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    mtc_name = models.CharField(max_length=255, null=True, blank=True)
    importance = models.FloatField(null=True, blank=True)
    softlinks = models.ManyToManyField('self')

    objects = models.GeoManager()
    
    def save(self, user=None, comment=""):           
        super(Stage, self).save()
        if user:
            sh = StageRevision(stage = self, 
                               display_name = self.display_name,
                               location=self.location,
                               user = user,
                               comment = comment
                               )
            sh.save()                                               
    
    def __unicode__(self):
        return self.display_name

class StageRevision(models.Model):
    stage = models.ForeignKey(Stage)
    edited_at = models.DateTimeField(auto_now_add=True)
    display_name = models.CharField(max_length=255)
    location = models.PointField(null=True, blank=True)
    user = models.ForeignKey(User)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    comment = models.CharField(max_length=1024, blank=True, null=True)
