import os

from django.core.management.base import BaseCommand, CommandError

import gpxpy.geo
import gpxpy.parser
import gpxpy.gpx

import togeojsontiles

from nswandel.stations.models import Station
from nswandel.trails.models import NSTrail
from nswandel.local_settings import STATIC_ROOT, TIPPECANOE_DIR


class Command(BaseCommand):
    help = 'create geojson for all trails'

    def handle(self, *args, **options):
        mbtiles_file = 'temp.mbtiles'
        geojsonfiles = []
        trails = NSTrail.objects.all()
        for trail in trails:
            if trail.gpx_file:
                gpxfilepath = trail.get_gpxfilepath()
                self.stdout.write(gpxfilepath)
                geojsonfilepath = os.path.join('static/data/geojson/', os.path.basename(gpxfilepath.replace('.gpx', '.geojson')))
                togeojsontiles.gpx_to_geojson(gpxfilepath, geojsonfilepath)
                geojsonfiles.append(geojsonfilepath)

        geojsonfiles.append('static/data/boundingbox.geojson')  # forces to generate a tile for every position within the bounding box, prevents 404, needs nicer solution
        togeojsontiles.geojson_to_mbtiles(
            filepaths=geojsonfiles,
            tippecanoe_dir=TIPPECANOE_DIR,
            mbtiles_file=mbtiles_file,
            maxzoom=13
        )

        tiles_dir = ('static/data/tiles/')
        togeojsontiles.mbtiles_to_geojsontiles(TIPPECANOE_DIR, tiles_dir, mbtiles_file)
        os.remove(mbtiles_file)
