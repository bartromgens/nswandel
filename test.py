import json


class Trail(object):
    def __init__(self, name='undefined'):
        self.name = name
        self.gpx_filename = 'amsterdam-amsterdam.gpx'

    def __str__(self):
        return self.name + ' - gpx: ' + self.gpx_filename

    @staticmethod
    def from_json(json_object):
        if 'gpx_filename' in json_object:
            trail = Trail()
            trail.name = json_object['name']
            trail.gpx_filename = json_object['gpx_filename']
            return trail
        else:
            return json_object


class Trails(object):
    def __init__(self):
        self.trails = []

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
    trails.append(Trail("test1"))
    trails.append(Trail("test2"))
    filename = 'trails.json'
    trails.to_json(filename)
    trails.from_json(filename)


if __name__ == "__main__":
    main()