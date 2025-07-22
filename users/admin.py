from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'window_number']
    list_filter = ['role']
    search_fields = ['user__username']

admin.site.register(UserProfile, UserProfileAdmin)
