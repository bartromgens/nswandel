from django.conf.urls import url, include
from django.contrib import admin

from nswandelingen.core.views import HomePageView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name ='home'),
    url(r'^trails/', include('nswandelingen.trails.urls')),
    url(r'^admin/', admin.site.urls),
]
