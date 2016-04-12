from django.shortcuts import render

from django.views.generic import TemplateView

from nswandel.trails.models import Trail


class TrailsView(TemplateView):
    template_name = 'trails/trail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trails = Trail.objects.all()
        context['trails'] = trails
        return context
