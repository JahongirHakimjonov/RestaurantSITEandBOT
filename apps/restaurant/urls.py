from django.urls import path
from .views import (
    HomeView,
    AboutView,
    ServiceView,
    MenuView,
    BookingView,
    TeamView,
    TestimonialView,
    ContactView,
)

app_name = "restaurant"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("service/", ServiceView.as_view(), name="service"),
    path("menu/", MenuView.as_view(), name="menu"),
    path("booking/", BookingView.as_view(), name="booking"),
    path("team/", TeamView.as_view(), name="team"),
    path("testimonial/", TestimonialView.as_view(), name="testimonial"),
    path("contact/", ContactView.as_view(), name="contact"),
]
