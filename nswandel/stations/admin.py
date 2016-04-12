from django.contrib import admin

from nswandel.stations.models import Station


class StationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['code']}),
        (None, {'fields': ['name_long']}),
    ]
    list_display = ('code', 'name_long')

admin.site.register(Station, StationAdmin)
