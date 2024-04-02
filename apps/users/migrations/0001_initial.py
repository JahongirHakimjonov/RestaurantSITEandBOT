# Generated by Django 5.0.3 on 2024-04-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BotUsers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("telegram_id", models.IntegerField(unique=True)),
                ("username", models.CharField(blank=True, max_length=255, null=True)),
                ("first_name", models.CharField(blank=True, max_length=255, null=True)),
                ("last_name", models.CharField(blank=True, max_length=255, null=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "language_code",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "role",
                    models.CharField(
                        choices=[("admin", "Admin"), ("user", "User")],
                        default="user",
                        max_length=10,
                    ),
                ),
            ],
            options={
                "verbose_name": "Bot User",
                "verbose_name_plural": "Bot Foydalanuvchilari",
                "db_table": "bot_users",
            },
        ),
        migrations.CreateModel(
            name="DailyMessages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("telegram_id", models.BigIntegerField()),
                ("message_date", models.DateField()),
                ("message_count", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "Kunlik xabarlar",
                "db_table": "daily_message",
            },
        ),
        migrations.CreateModel(
            name="SiteUsers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
            options={
                "verbose_name_plural": "Sayt Foydalanuvchilar",
                "db_table": "site_user",
            },
        ),
        migrations.CreateModel(
            name="TelegramChannelID",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("channel_id", models.IntegerField(unique=True)),
                ("channel_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Telegram Channel ID",
                "verbose_name_plural": "Telegram Channel IDs",
                "db_table": "telegram_channel_id",
            },
        ),
        migrations.CreateModel(
            name="TelegramGroupID",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("group_id", models.IntegerField(unique=True)),
                ("group_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Telegram Group ID",
                "verbose_name_plural": "Telegram Group IDs",
                "db_table": "telegram_group_id",
            },
        ),
    ]