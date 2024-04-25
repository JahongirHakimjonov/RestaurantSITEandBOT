from django.db import models
from apps.shared.models import AbstractBaseModel


class Emails(AbstractBaseModel):
    title = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"
        db_table = "emails"

    def __str__(self):
        return self.email


class PhoneNumbers(AbstractBaseModel):
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Phone Number"
        verbose_name_plural = "Phone Numbers"
        db_table = "phone_numbers"

    def __str__(self):
        return self.phone


class Home(AbstractBaseModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    phone = models.ForeignKey(
        PhoneNumbers,
        related_name="home_phone",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    email = models.ForeignKey(
        Emails,
        related_name="home_email",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    website = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    telegram = models.URLField()
    youtube = models.URLField()
    youtube_video = models.URLField()
    image = models.ImageField(upload_to="home/")
    logo = models.ImageField(upload_to="home/")

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"
        db_table = "home"

    def __str__(self):
        return self.name


class Gallery(AbstractBaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="gallery/")

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        db_table = "gallery"

    def __str__(self):
        return self.title


class About(AbstractBaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="about/")
    experience = models.IntegerField()
    master_chefs = models.IntegerField()

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
        db_table = "about"

    def __str__(self):
        return self.title


class MasterChef(AbstractBaseModel):
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    instagram = models.URLField()
    facebook = models.URLField()
    telegram = models.URLField()
    image = models.ImageField(upload_to="masterchef/", null=True, blank=True, default='/static/image/man.jpg')

    class Meta:
        verbose_name = "Master Chef"
        verbose_name_plural = "Master Chef"
        db_table = "master_chef"

    def __str__(self):
        return self.full_name


class Testimonial(AbstractBaseModel):
    full_name = models.CharField(max_length=255)
    description = models.TextField()
    profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to="testimonial/", null=True, blank=True, default='/static/image/profile.jpg')

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonial"
        db_table = "testimonial"

    def __str__(self):
        return self.full_name


class Services(AbstractBaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="services/", null=True, blank=True, default='/static/image/black_logo.png')

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        db_table = "services"

    def __str__(self):
        return self.title


class MenuType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Menu Type"
        verbose_name_plural = "Menu Types"
        db_table = "menu_type"


class Menu(models.Model):
    menu_type = models.ForeignKey(MenuType, related_name='menu_items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_images', null=True, blank=True, default='/static/image/food.jpg')

    def __str__(self):
        return self.title


class Reservation(AbstractBaseModel):
    GUESTS = (
        (1, "1 ta"),
        (2, "2 ta"),
        (3, "3 ta"),
        (4, "4 ta"),
        (5, "5 ta"),
        (6, "6 ta"),
        (7, "7 ta"),
        (8, "8 ta"),
        (9, "9 ta"),
        (10, "10 ta"),
        (11, "11 ta"),
        (12, "12 ta"),
        (13, "13 ta"),
        (14, "14 ta"),
        (15, "15 ta"),
        (16, "16 ta"),
        (17, "17 ta"),
        (18, "18 ta"),
        (19, "19 ta"),
        (20, "20 ta"),
    )
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    guests = models.IntegerField(choices=GUESTS)
    message = models.TextField()

    class Meta:
        verbose_name = "Book Table"
        verbose_name_plural = "Book Tables"
        db_table = "book_table"

    def __str__(self):
        return self.full_name


class ContactUs(AbstractBaseModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
        db_table = "contact_us"

    def __str__(self):
        return self.full_name


class NewsLetter(AbstractBaseModel):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = "News Letter"
        verbose_name_plural = "News Letters"
        db_table = "news_letter"

    def __str__(self):
        return self.email


class WorkTime(AbstractBaseModel):
    day = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = "Work Time"
        verbose_name_plural = "Work Times"
        db_table = "work_time"

    def __str__(self):
        return self.day
