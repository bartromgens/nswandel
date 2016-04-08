
// http://stackoverflow.com/a/4234006
$.ajaxSetup({beforeSend: function(xhr){
    if (xhr.overrideMimeType)
    {
      xhr.overrideMimeType("application/json");
    }
}
});

var map = new ol.Map({target: 'map'});
var view = new ol.View( {center: [0, 0], zoom: 10, projection: 'EPSG:3857'} );
map.setView(view);

var osmSource = new ol.source.OSM("OpenStreetMap");
osmSource.setUrl("http://a.tile.openstreetmap.org/{z}/{x}/{y}.png ");
var osmLayer = new ol.layer.Tile({source: osmSource});

map.addLayer(osmLayer);

var lon = '5.1';
var lat = '142.0';
view.setCenter(ol.proj.fromLonLat([lon, lat]));

// Controls
map.addControl(new ol.control.FullScreen());


// GPX tracks

var style = {
    // Points are hidden
    'Point': [new ol.style.Style({
        image: new ol.style.Circle({
            fill: new ol.style.Fill({
                color: 'rgba(255,255,0,0.4)'
            }),
            radius: 0,
            stroke: new ol.style.Stroke({
                color: '#ff0',
                width: 0
            })
        })
    })],
    'LineString': [new ol.style.Style({
        stroke: new ol.style.Stroke({
            color: 'green',
            width: 5
        })
    })],
    'MultiLineString': [new ol.style.Style({
        stroke: new ol.style.Stroke({
            color: 'green',
            width: 5
        })
    })]
};


function createTrailLayer(json_trail)
{
    var trackVector = new ol.layer.Vector({
        source: new ol.source.Vector({
            projection: 'EPSG:3857',
            format: new ol.format.GPX(),
            url: './data/gpx/' + json_trail.gpx_filename
        }),
        style: function(feature, resolution) {
            return style[feature.getGeometry().getType()];
        }
    });
    return trackVector;
}


$.getJSON("./trails_downloaded.json", function(json) {
    console.log(json.trails);
    for (var i in json.trails)
    {
        var trail = json.trails[i];
        console.log(trail)
        trail = createTrailLayer(trail);
        map.addLayer(trail);
    }
});