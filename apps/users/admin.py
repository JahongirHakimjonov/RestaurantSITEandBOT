from django.contrib import admin
from apps.users.models import (
    BotUsers,
    TelegramGroupID,
    TelegramChannelID,
    DailyMessages,
    SiteUsers,
)


@admin.register(BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ("username", "telegram_id", "role", "is_active")
    list_filter = ("role", "is_active")
    search_fields = ("username", "telegram_id")


@admin.register(TelegramGroupID)
class TelegramGroupIDAdmin(admin.ModelAdmin):
    list_display = ("group_id", "group_name")
    search_fields = ("group_id", "group_name")


@admin.register(TelegramChannelID)
class TelegramChannelIDAdmin(admin.ModelAdmin):
    list_display = ("channel_id", "channel_name")
    search_fields = ("channel_id", "channel_name")


@admin.register(DailyMessages)
class DailyMessagesAdmin(admin.ModelAdmin):
    list_display = ("telegram_id", "message_date", "message_count")
    search_fields = ("telegram_id", "message_date")


@admin.register(SiteUsers)
class SiteUsersAdmin(admin.ModelAdmin):
    list_display = ("useremail",)
    search_fields = ("useremail",)
