from django.db import models


class Trail(models.Model):
    title = models.CharField(max_length=300)
    gpx_file = models.FileField()

    def __str__(self):
        return self.title
