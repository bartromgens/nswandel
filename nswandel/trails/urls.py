from django.conf.urls import url
from django.contrib import admin

from nswandel.trails.views import TrailsView


urlpatterns = [
    url(r'^$', TrailsView.as_view(), name ='trails'),
    url(r'^admin/', admin.site.urls),
]