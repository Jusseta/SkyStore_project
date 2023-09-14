from django.contrib import admin
from mailing.models import Client, MailingLogs, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'full_name', 'email',)
    search_fields = ('full_name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'theme', 'body', 'time', 'frequency', 'status',)
    search_fields = ('theme',)


@admin.register(MailingLogs)
class MailingLogsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'last_try', 'status',)
    search_fields = ('status',)
