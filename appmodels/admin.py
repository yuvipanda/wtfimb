from appmodels.models import *
from django.contrib import admin

class StageAdmin(admin.ModelAdmin):
	list_display = ('display_name', 'latitude', 'longitude')

class RouteAdmin(admin.ModelAdmin):
	list_display = ('display_name', 'types', 'start', 'end', 'has_unmapped_stages')

	def has_unmapped_stages(self, obj):
		for s in obj.stages.all():
			if not s.latitude:
				return True
		return False
	has_unmapped_stages.boolean = True

class StageRevisionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Route, RouteAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(StageRevision, StageRevisionAdmin)
