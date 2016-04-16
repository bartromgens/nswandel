from django.db import models


class StationType(object):
    MEGA = 'megastation'
    INTERCITY = 'intercitystation'
    INTERCITY_KNOOP = 'knooppuntIntercitystation'
    SNELTREIN = 'sneltreinstation'
    SNELTREIN_KNOOP = 'knooppuntSneltreinstation'
    STOPTREIN = 'stoptreinstation'
    STOPTREIN_KNOOP = 'knooppuntStoptreinstation'
    FACULTATIEF = 'facultatiefStation'

    STATION_TYPE_CHOICES = (
        (MEGA, 'megastation'),
        (INTERCITY, 'intercitystation'),
        (INTERCITY_KNOOP, 'knooppuntIntercitystation'),
        (SNELTREIN, 'sneltreinstation'),
        (SNELTREIN_KNOOP, 'knooppuntSneltreinstation'),
        (STOPTREIN, 'stoptreinstation'),
        (STOPTREIN_KNOOP, 'knooppuntStoptreinstation'),
        (FACULTATIEF, 'facultatiefStation'),
    )


class Station(models.Model):
    code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    type = models.CharField(max_length=100, choices=StationType.STATION_TYPE_CHOICES, default=StationType.STOPTREIN)
    name_long = models.CharField(max_length=200)
    name_middle = models.CharField(max_length=150)
    name_short = models.CharField(max_length=100)

    def __str__(self):
        return self.code
