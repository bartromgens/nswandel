from django.contrib import admin

from nswandel.trails.models import Trail, NSTrail


trail_fields = (None, {'fields': ['title', 'gpx_file']})


class TrailAdmin(admin.ModelAdmin):
    fieldsets = [
        trail_fields,
    ]
    list_display = ('title',)


class NSTrailAdmin(TrailAdmin):
    fieldsets = [
        trail_fields,
        (None, {'fields': ['station_begin', 'station_end']}),
    ]
    list_display = ('id', 'title', 'station_begin', 'station_end')


admin.site.register(Trail, TrailAdmin)
admin.site.register(NSTrail, NSTrailAdmin)
