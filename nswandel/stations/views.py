from django.shortcuts import render

from django.views.generic import TemplateView

from nswandel.stations.models import Station


class StationView(TemplateView):
    template_name = 'stations/stations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stations = Station.objects.all()
        context['stations'] = stations
        return context
