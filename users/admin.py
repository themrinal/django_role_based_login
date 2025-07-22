# Import the Django admin module which allows model data to be managed through a web interface
from django.contrib import admin

# Import the custom model 'UserProfile' that holds user roles and extra info
from .models import UserProfile

# Create a custom admin class to control how UserProfile appears in the Django admin panel
class UserProfileAdmin(admin.ModelAdmin):
    # This defines which fields will be displayed in the list view of the admin panel
    list_display = ['user', 'role', 'window_number']
    
    # This adds a filter sidebar by 'role' so admin users can quickly filter by user type
    list_filter = ['role']
    
    # This enables a search box that can search by the related User model's username
    # The double underscore (__) lets us reach into the related User model
    search_fields = ['user__username']

# Finally, register the UserProfile model with the admin site
# This makes it accessible from the Django admin interface and applies the custom display settings
admin.site.register(UserProfile, UserProfileAdmin)
