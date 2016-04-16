from django.contrib import admin

from nswandel.stations.models import Station


class StationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['code']}),
        (None, {'fields': ['name_long', 'name_middle', 'name_short']}),
        (None, {'fields': ['latitude', 'longitude']}),
        (None, {'fields': ['type']}),
    ]
    list_display = ('code', 'name_long', 'type')

admin.site.register(Station, StationAdmin)
