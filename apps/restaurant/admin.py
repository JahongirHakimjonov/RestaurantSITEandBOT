from django.contrib import admin
from apps.restaurant.models import (
    About,
    Emails,
    Home,
    PhoneNumbers,
    MasterChef,
    Testimonial,
    Services,
    MenuType,
    Menu,
    Reservation,
    ContactUs,
    Gallery,
    NewsLetter,
    WorkTime,
)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title", "description")
    list_filter = ("title", "description")


@admin.register(Emails)
class EmailsAdmin(admin.ModelAdmin):
    list_display = ("email", "title")
    search_fields = ("email", "title")
    list_filter = ("email",)


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "title",
        "description",
        "address",
        "phone",
        "email",
        "website",
        "facebook",
        "instagram",
        "twitter",
        "telegram",
        "youtube",
        "logo",
    )
    search_fields = (
        "name",
        "title",
        "description",
        "address",
        "phone",
        "email",
        "website",
        "facebook",
        "instagram",
        "twitter",
        "telegram",
        "youtube",
    )


@admin.register(PhoneNumbers)
class PhoneNumbersAdmin(admin.ModelAdmin):
    list_display = ("phone", "title")
    search_fields = ("phone", "title")
    list_filter = ("phone",)


@admin.register(MasterChef)
class MasterChefAdmin(admin.ModelAdmin):
    list_display = ("full_name", "role")
    search_fields = ("full_name", "role")
    list_filter = ("full_name", "role")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("full_name", "description", "profession")
    search_fields = ("full_name", "description")
    list_filter = ("full_name", "description")


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title", "description")
    list_filter = ("title", "description")


@admin.register(MenuType)
class MenuTypeAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = ("title",)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price", "menu_type")
    search_fields = ("title", "description", "price", "menu_type")
    list_filter = ("title", "description", "price", "menu_type")


@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "datetime", "guests", "message")
    search_fields = ("full_name", "email", "phone", "datetime", "guests", "message")


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject", "message")
    list_filter = ("full_name", "email", "subject")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title", "description")
    list_filter = ("title", "description")


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ("email",)
    search_fields = ("email",)
    list_filter = ("email",)


@admin.register(WorkTime)
class WorkTimeAdmin(admin.ModelAdmin):
    list_display = ("day", "start_time", "end_time")
    search_fields = ("day", "start_time", "end_time")
    list_filter = ("day", "start_time", "end_time")
