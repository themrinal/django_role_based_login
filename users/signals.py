# Import Django's signal that fires after a model instance is saved
from django.db.models.signals import post_save

# Import the receiver decorator to handle signals
from django.dispatch import receiver

# Import Django's built-in User model
from django.contrib.auth.models import User

# Import the custom UserProfile model
from .models import UserProfile

# This function listens for when a new User object is created
# It runs automatically right after a User is saved (post_save)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Check if this is a new User object being created (not just updated)
    if created:
        # Automatically create a linked UserProfile for the new User
        UserProfile.objects.create(user=instance)
