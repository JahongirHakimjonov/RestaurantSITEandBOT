# Generated by Django 5.0.3 on 2024-04-05 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="menu",
            options={},
        ),
        migrations.AlterField(
            model_name="menu",
            name="image",
            field=models.ImageField(
                blank=True,
                default="/static/image/food.jpg",
                null=True,
                upload_to="menu_images",
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="menu_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="menu_items",
                to="restaurant.menutype",
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name="menu",
            name="title",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="menutype",
            name="title",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name="menu",
            table=None,
        ),
    ]