from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ('user', 'user_code')
    search_fields = ('user', 'user_code')
