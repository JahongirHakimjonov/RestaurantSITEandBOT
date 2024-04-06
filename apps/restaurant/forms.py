from apps.restaurant.models import Reservation, ContactUs
from django import forms

from apps.users.models import SiteUsers


class ReservationCreateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["full_name", "email", "phone", "datetime", "guests", "message"]
        widgets = {
            "datetime": forms.DateInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                    "id": "datetime",
                    "placeholder": "Sana va vaqt tanlang",
                }
            ),
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "id": "name", "placeholder": "Ismingiz"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "placeholder": "Emailingiz",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "phone",
                    "placeholder": "Telefon raqamingiz",
                }
            ),
            "guests": forms.Select(
                attrs={
                    "class": "form-select",
                    "id": "select1",
                    "aria-label": "Mehmonlar soni tanlang",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Qo'shimcha talablaringizni yozing",
                    "id": "message",
                    "style": "height: 100px",
                }
            ),
        }


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["full_name", "email", "subject", "message"]
        widgets = {
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "id": "name", "placeholder": "Ismingiz"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "placeholder": "Emailingiz",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "subject",
                    "placeholder": "Sarlavha",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Xabaringizni yozib qoldiring",
                    "id": "message",
                    "style": "height: 100px",
                }
            ),
        }


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = SiteUsers
        fields = ["useremail"]
        widgets = {
            "useremail": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "placeholder": "Emailingiz",
                }
            ),
        }
