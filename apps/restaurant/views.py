from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Home


class HomeView(TemplateView):
    template_name = "restaurant/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = Home.objects.first()
        return context
