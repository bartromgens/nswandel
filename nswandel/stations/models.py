from django.db import models


class StationType(object):
    MEGA = 'MEG'
    INTERCITY = 'IC'
    INTERCITY_KNOOP = 'ICK'
    SNELTREIN = 'SNT'
    SNELTREIN_KNOOP = 'SNK'
    STOPTREIN = 'ST'
    STOPTREIN_KNOOP = 'STK'
    FACULTATIEF = 'FAC'

    STATION_TYPE_CHOICES = (
        (MEGA, 'megastation'),
        (INTERCITY, 'intercitystation'),
        (INTERCITY_KNOOP, 'knooppuntIntercitystation'),
        (SNELTREIN, 'sneltreinstation'),
        (SNELTREIN_KNOOP, 'knooppuntSneltreinstation'),
        (STOPTREIN_KNOOP, 'knooppuntStoptreinstation'),
        (STOPTREIN, 'stoptreinstation'),
        (FACULTATIEF, 'facultatiefStation'),
    )


class Station(models.Model):
    code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    type = models.CharField(max_length=3, choices=StationType.STATION_TYPE_CHOICES, default=StationType.STOPTREIN)
    name_long = models.CharField(max_length=200)
    name_middle = models.CharField(max_length=150)
    name_short = models.CharField(max_length=100)
    sdfd = models.CharField(max_length=10)

    def __str__(self):
        return self.code
