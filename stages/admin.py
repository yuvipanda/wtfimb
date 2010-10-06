from models import Stage
from django.contrib.gis import admin
from reversion.admin import VersionAdmin
from routes.models import RouteStage
from django.core.urlresolvers import reverse

class RouteStageInline(admin.TabularInline):
    model = RouteStage 
    extra = 1 
    ordering = ['stage__display_name']

class StageAdmin(admin.OSMGeoAdmin,VersionAdmin):
    list_display = ('display_name',
                    'view_stage_link',
                    'city',
                    'location', 
                    )
    ordering = ['city', 'display_name']
    def view_stage_link(self, obj):
        return "<a href='%s'>View</a>" % reverse('show-stage', args=[obj.city, obj.id])

    view_stage_link.allow_tags = True
    view_stage_link.short_description = "Link to Site"

    inlines = (RouteStageInline, )

    search_fields = ['display_name']


admin.site.register(Stage, StageAdmin)
