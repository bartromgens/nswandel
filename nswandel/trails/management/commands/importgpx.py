import os
import fnmatch

from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import File

from nswandel.trails.models import NSTrail


class Command(BaseCommand):
    help = 'import gpx files in a given directory'

    def add_arguments(self, parser):
        parser.add_argument('gpxdir', type=str)

    def handle(self, *args, **options):
        gpx_dir = options['gpxdir']
        self.stdout.write(gpx_dir)
        for root, subFolders, filenames in os.walk(gpx_dir):
            for filename in fnmatch.filter(filenames, '*.gpx'):
                filepath = os.path.join(root, filename)
                self.stdout.write(filepath)
                trail = NSTrail.objects.create()
                trail.title = "undefined"
                gpxfile = open(filepath)
                trail.gpx_file.save(filename, File(gpxfile))
                trail.save()
