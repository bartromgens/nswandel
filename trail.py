import json


class Trail(object):
    def __init__(self, name='undefined', gpx_filename='undefined.json', url_extern='http://www.nlwandel.nl'):
        self.name = name
        self.gpx_filename = gpx_filename
        self.url_extern = url_extern

    def __str__(self):
        return self.name + ' - gpx: ' + self.gpx_filename

    @staticmethod
    def from_json(json_object):
        if 'gpx_filename' in json_object:
            trail = Trail()
            trail.name = json_object['name']
            trail.gpx_filename = json_object['gpx_filename']
            trail.url_extern = json_object['url_extern']
            return trail
        else:
            return json_object


class Trails(object):
    def __init__(self):
        self.trails = []

    def __iter__(self):
        return self.trails.__iter__()

    def append(self, trail):
        self.trails.append(trail)

    def to_json(self, filepath='trails.json'):
        trails = {'trails': self.trails}
        json_dump = json.dumps(trails, cls=TrailJSONEncoder, indent=4, sort_keys=True, ensure_ascii=False)
        print(json_dump)
        with open(filepath, 'w') as fileout:
            fileout.write(json_dump)

    @staticmethod
    def from_json(filepath='trails.json'):
        with open(filepath, 'r') as filein:
            jsonin = json.load(filein, object_hook=Trail.from_json)
        for trail in jsonin['trails']:
            print(trail)


class TrailJSONEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def main():
    print('main() - START!')
    trails = Trails()
    trails.append(Trail('Amsterdam - Amsterdam', 'amsterdam-amsterdam.gpx'))
    trails.append(Trail('Bussum Zuid - Weesp', 'bussum_zuid-weesp.gpx'))
    trails.append(Trail('Ede-Wageningen - Wageningen', 'ede-wageningen-wageningen.gpx'))
    filename = 'trails.json'
    trails.to_json(filename)
    trails.from_json(filename)


if __name__ == "__main__":
    main()