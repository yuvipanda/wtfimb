from django.db import models

from django.contrib.auth.models import User

class Stage(models.Model):
    display_name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    mtc_name = models.CharField(max_length=255, null=True, blank=True)
    #routes = models.ManyToManyField('Route') #Since Route isn't yet defined
    importance = models.FloatField(null=True, blank=True)
    softlinks = models.ManyToManyField('self')

    def save(self, user=None, comment=""):           
        super(Stage, self).save()
        if user:
            sh = StageRevision(stage = self, 
                               display_name = self.display_name,
                               latitude = self.latitude,
                               longitude = self.longitude,
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
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=1024, blank=True, null=True)
