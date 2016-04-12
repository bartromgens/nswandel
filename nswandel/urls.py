from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers, serializers, viewsets

from nswandel.core.views import HomePageView
from nswandel.trails.models import Trail


# Serializers define the API representation.
class TrailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trail
        fields = ('title', 'gpx_file')


# ViewSets define the view behavior.
class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'trails', TrailViewSet)


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name ='home'),
    url(r'^trails/', include('nswandel.trails.urls')),
    url(r'^stations/', include('nswandel.stations.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
