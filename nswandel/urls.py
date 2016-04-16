from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers, serializers, viewsets

from nswandel.core.views import HomePageView
from nswandel.trails.models import Trail, NSTrail
from nswandel.stations.models import Station


# Serializers define the API representation.
class TrailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trail
        fields = ('title', 'gpx_file')


# ViewSets define the view behavior.
class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer


# Serializers define the API representation.
class NSTrailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NSTrail
        fields = ('title', 'gpx_file', 'station_begin', 'station_end')


# ViewSets define the view behavior.
class NSTrailViewSet(viewsets.ModelViewSet):
    queryset = NSTrail.objects.all()
    serializer_class = NSTrailSerializer


# Serializers define the API representation.
class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'code', 'latitude', 'longitude', 'name_long', 'name_middle', 'name_short', 'type')


# ViewSets define the view behavior.
class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'trails', TrailViewSet)
router.register(r'nstrails', NSTrailViewSet)
router.register(r'stations', StationViewSet)


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name ='home'),
    url(r'^trails/', include('nswandel.trails.urls')),
    url(r'^stations/', include('nswandel.stations.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
