from django.views.generic import TemplateView, ListView

from .models import Home, WorkTime


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = Home.objects.first()
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = Home.objects.first()
        return context


class ServiceView(TemplateView):
    template_name = "service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = Home.objects.first()
        return context


class MenuView(TemplateView):
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = Home.objects.first()
        return context


class BookingView(TemplateView):
    template_name = "booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = Home.objects.first()
        return context


class TeamView(TemplateView):
    template_name = "team.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = Home.objects.first()
        return context


class TestimonialView(TemplateView):
    template_name = "testimonial.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = Home.objects.first()
        return context


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = Home.objects.first()
        return context


def worktimes(request):
    worktimes = WorkTime.objects.all()
    return {
        'worktimes': worktimes
    }


def contacts(request):
    home = Home.objects.first()
    return {
        'home': home
    }
