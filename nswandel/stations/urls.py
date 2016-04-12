from django.conf.urls import url, include
from django.contrib import admin

from nswandel.stations.views import StationView


urlpatterns = [
    url(r'^$', StationView.as_view(), name='stations'),
    url(r'^admin/', admin.site.urls),
]