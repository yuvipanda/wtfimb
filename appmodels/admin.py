from appmodels.models import *
from django.contrib import admin
from reversion.admin import VersionAdmin

class RouteStageInline(admin.TabularInline):
	model = RouteStage 
	extra = 1 

class StageAdmin(admin.ModelAdmin):
	list_display = ('display_name', 
					'latitude', 
					'longitude', 
					)

	inlines = (RouteStageInline, )


class RouteAdmin(admin.ModelAdmin):
	list_display = ('display_name', 'types', 'start', 'end', 'has_unmapped_stages')

	def has_unmapped_stages(self, obj):
		for s in obj.stages.all():
			if not s.latitude:
				return True
		return False
	has_unmapped_stages.boolean = True

	inlines = (RouteStageInline, )


admin.site.register(Route, RouteAdmin)
admin.site.register(Stage, StageAdmin)
