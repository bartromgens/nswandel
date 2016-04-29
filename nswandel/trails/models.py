import os

from django.db import models

from nswandel.local_settings import MEDIA_ROOT


class Trail(models.Model):
    title = models.CharField(max_length=300)
    distance = models.FloatField(blank=True, null=True, help_text='distance in m')
    gpx_file = models.FileField(upload_to='gpx/')

    def get_gpxfilepath(self):
        return os.path.join(MEDIA_ROOT, self.gpx_file.path)

    def __str__(self):
        return self.title


class NSTrail(Trail):
    station_begin = models.ForeignKey('stations.Station', related_name='station_begin', blank=True, null=True)
    station_end = models.ForeignKey('stations.Station', related_name='station_end', blank=True, null=True)
