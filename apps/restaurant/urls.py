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
    site_user,
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
    path("site_user/", site_user, name="site_user"),
]
