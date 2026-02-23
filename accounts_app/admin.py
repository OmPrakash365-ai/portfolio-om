from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'name', 'skills')

    search_fields = ('user__username', 'skills')

    list_filter = ('user',)