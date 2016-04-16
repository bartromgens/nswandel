from django.db import models


class Trail(models.Model):
    title = models.CharField(max_length=300)
    gpx_file = models.FileField(upload_to='gpx/')

    def __str__(self):
        return self.title


class NSTrail(Trail):
    station_begin = models.ForeignKey('stations.Station', related_name='station_begin', blank=True, null=True)
    station_end = models.ForeignKey('stations.Station', related_name='station_end', blank=True, null=True)
