from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'timestamp')
    search_fields = ('name', 'email', 'message')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
    list_per_page = 20