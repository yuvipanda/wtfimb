from django.db import models

class Stage(models.Model):
	display_name = models.CharField(max_length=255)
	lattitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	mtc_name = models.CharField(max_length=255)
	#routes = models.ManyToManyField('Route') #Since Route isn't yet defined

class Route(models.Model):
	display_name = models.CharField(max_length=64)
	mtc_name = models.CharField(max_length=64)
	types = models.CharField(max_length=64)
	start = models.ForeignKey(Stage, related_name='start')
	end = models.ForeignKey(Stage, related_name='end')
	stages = models.ManyToManyField(Stage)
	time = models.FloatField()
	fare = models.FloatField()

# Create your models here.
