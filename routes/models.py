from django.contrib.gis.db import models
from django.template.defaultfilters import slugify

ROUTE_TYPE_CHOICES = (
    ('T', 'Train'),
    ('B', 'Bus'),
    )
    
ROUTE_TYPE_MAPPING = {
        'DLX': 'Deluxe',
        'AC': 'Air Conditioned',
        'EXP': 'Express',
        'NGT': 'Night Service',
        'MSVC': 'M Service',
        'ORD': 'Ordinary',
        'LSS': 'Limited Stop Service',
        'VAJ': 'Vajra',
        'BIAS': 'BIAS - Vayu Vajra',
        'B10': 'Big 10',
        }
class Route(models.Model):
    display_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, default='')
    mtc_name = models.CharField(max_length=64)
    types = models.CharField(max_length=64)
    start = models.ForeignKey('stages.Stage', related_name='start_for_routes')
    end = models.ForeignKey('stages.Stage', related_name='end_for_routes')
    stages = models.ManyToManyField('stages.Stage', through="RouteStage")
    time = models.FloatField()
    fare = models.FloatField()
    type = models.CharField(max_length=1, choices=ROUTE_TYPE_CHOICES, default='B')
    city = models.CharField(max_length=255)

    class Meta:
       ordering = ['slug',]
    def __unicode__(self):
        return self.display_name

class RouteStage(models.Model):
    route = models.ForeignKey(Route)
    stage = models.ForeignKey('stages.Stage', related_name='routelinks')
    sequence = models.IntegerField()

    def __unicode__(self):
        return (str)(self.route)+'|'+(str)(self.sequence)+'.'+(str)(self.stage)
