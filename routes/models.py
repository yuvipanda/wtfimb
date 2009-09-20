from django.db import models

class Route(models.Model):
    display_name = models.CharField(max_length=64)
    mtc_name = models.CharField(max_length=64)
    types = models.CharField(max_length=64)
    start = models.ForeignKey('stages.Stage', related_name='start_for_routes')
    end = models.ForeignKey('stages.Stage', related_name='end_for_routes')
    stages = models.ManyToManyField('stages.Stage', through="RouteStage")
    time = models.FloatField()
    fare = models.FloatField()

    def __unicode__(self):
        return self.display_name

class RouteStage(models.Model):
    route = models.ForeignKey(Route)
    stage = models.ForeignKey('stages.Stage', related_name='routelinks')
    sequence = models.IntegerField()

