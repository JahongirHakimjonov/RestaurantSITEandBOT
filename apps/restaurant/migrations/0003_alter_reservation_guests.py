# Generated by Django 5.0.3 on 2024-04-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_newsletter_message_newsletter_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="guests",
            field=models.IntegerField(
                choices=[
                    (1, "1 Guest"),
                    (2, "2 Guests"),
                    (3, "3 Guests"),
                    (4, "4 Guests"),
                    (5, "5 Guests"),
                    (6, "6 Guests"),
                    (7, "7 Guests"),
                    (8, "8 Guests"),
                    (9, "9 Guests"),
                    (10, "10 Guests"),
                    (11, "11 Guests"),
                    (12, "12 Guests"),
                    (13, "13 Guests"),
                    (14, "14 Guests"),
                    (15, "15 Guests"),
                    (16, "16 Guests"),
                    (17, "17 Guests"),
                    (18, "18 Guests"),
                    (19, "19 Guests"),
                    (20, "20 Guests"),
                ]
            ),
        ),
    ]