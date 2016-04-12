from django.contrib import admin

from nswandel.trails.models import Trail


class TrailAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['gpx_file']}),
    ]
    list_display = ('title',)

admin.site.register(Trail, TrailAdmin)
