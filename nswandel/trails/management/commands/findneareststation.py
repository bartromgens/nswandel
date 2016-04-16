import os

from django.core.management.base import BaseCommand, CommandError

import gpxpy.geo
import gpxpy.parser
import gpxpy.gpx

from nswandel.stations.models import Station
from nswandel.trails.models import NSTrail
from nswandel.local_settings import MEDIA_ROOT


class Command(BaseCommand):
    help = 'finds the nearest stations for a all trails'

    # def add_arguments(self, parser):
    #     parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        trails = NSTrail.objects.all()
        for trail in trails:
            gpxfilepath = os.path.join(MEDIA_ROOT, trail.gpx_file.path)
            self.stdout.write(gpxfilepath)
            with open(gpxfilepath, 'r') as gpx_file:
                try:
                    gpx_parser = gpxpy.parser.GPXParser(gpx_file)
                    gpx = gpx_parser.parse()
                except gpxpy.gpx.GPXXMLSyntaxException as e:
                    self.stdout.write(str(e))
                    continue
                self.stdout.write('gpx file parsed')

                stations = Station.objects.all()
                station_nearest_begin = None
                station_nearest_end = None
                min_distance_begin = 1e99
                min_distance_end = 1e99

                for station in stations:
                    if gpx.routes:
                        point_begin = gpx.routes[0].points[0]
                        point_end = gpx.routes[-1].points[-1]
                    if gpx.tracks:
                        point_begin = gpx.tracks[0].segments[0].points[0]
                        point_end = gpx.tracks[-1].segments[-1].points[-1]

                    distance = gpxpy.geo.haversine_distance(point_begin.latitude, point_begin.longitude, float(station.latitude), float(station.longitude))
                    if distance < min_distance_begin:
                        min_distance_begin = distance
                        station_nearest_begin = station
                    distance = gpxpy.geo.haversine_distance(point_end.latitude, point_end.longitude, float(station.latitude), float(station.longitude))
                    if distance < min_distance_end:
                        min_distance_end = distance
                        station_nearest_end = station

                self.stdout.write(str(station_nearest_begin))
                self.stdout.write(str(station_nearest_end))
                self.stdout.write(str(min_distance_begin))
                self.stdout.write(str(min_distance_end))
                trail.title = station_nearest_begin.name_middle + ' - ' + station_nearest_end.name_middle
                trail.station_begin = station_nearest_begin
                trail.station_end = station_nearest_end
                trail.save()