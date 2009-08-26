from models import Route RouteStage
from django.contrib import admin

class RouteStageInline(admin.TabularInline):
    model = RouteStage 
    extra = 1 
    ordering = ['stage__display_name']

class RouteAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'route_view_link', 'types', 'start', 'end', 'has_unmapped_stages')

    def has_unmapped_stages(self, obj):
        for s in obj.stages.all():
            if not s.latitude:
                return True
        return False
    has_unmapped_stages.boolean = True

    def route_view_link(self, obj):
        return '<a href="/chennai/route/%s">View</a>' % obj.id

    route_view_link.allow_tags = True
    route_view_link.short_description = "Link to Site"

    inlines = (RouteStageInline, )

admin.site.register(Route, RouteAdmin)
