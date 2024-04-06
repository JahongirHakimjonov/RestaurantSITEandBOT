from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView

from .forms import ReservationCreateForm, ContactCreateForm, UserCreateForm
from .models import (
    Home,
    WorkTime,
    About,
    Gallery,
    Reservation,
    ContactUs,
    Emails,
    Testimonial,
    MasterChef,
    Menu,
    MenuType,
    Services,
)

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from apps.users.models import SiteUsers


class HomeView(FormView):
    template_name = "index.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("restaurant:home")

    def form_valid(self, form):
        useremail = form.cleaned_data.get("useremail")

        SiteUsers.objects.create(
            useremail=useremail
        )
        messages.success(
            self.request,
            "Ro'yxatdan o'tdingiz, tez orada siz bilan bog'lanishadi. Rahmat!",
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = Services.objects.all()
        context["about"] = About.objects.first()
        context["gallery"] = Gallery.objects.filter(title="Restoran")
        context["team"] = MasterChef.objects.all()
        context["testimonial"] = Testimonial.objects.all()
        return context


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactCreateForm
    success_url = reverse_lazy("restaurant:contact")

    def form_valid(self, form):
        full_name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        ContactUs.objects.create(
            full_name=full_name, email=email, subject=subject, message=message
        )
        messages.success(
            self.request,
            "Xabaringiz qabul qilindi, hodimlarimiz tez orada siz bilan bog'lanishadi. Rahmat!",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseBadRequest(
            render(self.request, self.template_name, {"form": form})
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["emails"] = Emails.objects.all()
        return context


class AboutView(FormView):
    template_name = "about.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("restaurant:about")

    def form_valid(self, form):
        useremail = form.cleaned_data.get("useremail")

        SiteUsers.objects.create(
            useremail=useremail
        )
        messages.success(
            self.request,
            "Ro'yxatdan o'tdingiz, tez orada siz bilan bog'lanishadi. Rahmat!",
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()
        context["gallery"] = Gallery.objects.filter(title="Restoran")
        return context


class ServiceView(FormView):
    template_name = "service.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("restaurant:service")

    def form_valid(self, form):
        useremail = form.cleaned_data.get("useremail")

        SiteUsers.objects.create(
            useremail=useremail
        )
        messages.success(
            self.request,
            "Ro'yxatdan o'tdingiz, tez orada siz bilan bog'lanishadi. Rahmat!",
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = Services.objects.all()
        return context


class MenuView(ListView):
    template_name = 'menu.html'
    context_object_name = 'menu_types'
    form_class = UserCreateForm
    success_url = reverse_lazy("restaurant:menu")

    def form_valid(self, form):
        useremail = form.cleaned_data.get("useremail")

        SiteUsers.objects.create(
            useremail=useremail
        )
        messages.success(
            self.request,
            "Ro'yxatdan o'tdingiz, tez orada siz bilan bog'lanishadi. Rahmat!",
        )
        return super().form_valid(form)

    def get_queryset(self):
        return MenuType.objects.all()


class BookingView(FormView):
    template_name = "booking.html"
    form_class = ReservationCreateForm
    success_url = reverse_lazy("restaurant:booking")

    def form_valid(self, form):
        datetime = form.cleaned_data.get("datetime")
        full_name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        phone = form.cleaned_data.get("phone")
        guests = form.cleaned_data.get("guests")
        message = form.cleaned_data.get("message")

        Reservation.objects.create(
            datetime=datetime,
            full_name=full_name,
            email=email,
            phone=phone,
            guests=guests,
            message=message,
        )
        messages.success(
            self.request,
            "Buyurtmangiz qabul qilindi, hodimlarimiz tez orada siz bilan bog'lanishadi. Rahmat!",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseBadRequest(
            render(self.request, self.template_name, {"form": form})
        )


class TeamView(FormView):
    template_name = "team.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("restaurant:team")

    def form_valid(self, form):
        useremail = form.cleaned_data.get("useremail")

        SiteUsers.objects.create(
            useremail=useremail
        )
        messages.success(
            self.request,
            "Ro'yxatdan o'tdingiz, tez orada siz bilan bog'lanishadi. Rahmat!",
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team"] = MasterChef.objects.all()
        return context


class TestimonialView(FormView):
    template_name = "testimonial.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("restaurant:testimonial")

    def form_valid(self, form):
        useremail = form.cleaned_data.get("useremail")

        SiteUsers.objects.create(
            useremail=useremail
        )
        messages.success(
            self.request,
            "Ro'yxatdan o'tdingiz, tez orada siz bilan bog'lanishadi. Rahmat!",
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonial"] = Testimonial.objects.all()
        return context


def worktimes(request):
    worktime = WorkTime.objects.all()
    return {"worktime": worktime}


def contacts(request):
    home = Home.objects.first()
    return {"home": home}
