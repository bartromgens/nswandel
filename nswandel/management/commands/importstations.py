import json

from django.core.management.base import BaseCommand, CommandError

from nswandel.stations.models import Station, StationType


class Command(BaseCommand):
    help = 'Imports stations from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        json_filepath = options['json_file'][1]
        with open(json_filepath, 'r') as filein:
            jsonin = json.load(filein)
            for station in jsonin['stations']:
                self.stdout.write(station['id'])
                station_new = Station()
                station_new.code = station['id']
                station_new.latitude = station['lat']
                station_new.longitude = station['lon']
                station_new.type = station['type']
                station_new.name_long = station['names']['long']
                station_new.name_middle = station['names']['middle']
                station_new.name_short = station['names']['short']
                station_new.save()