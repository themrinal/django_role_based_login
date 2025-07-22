# Import Django's model system
from django.db import models

# Import the built-in User model provided by Django for authentication
from django.contrib.auth.models import User 

# Define a custom model to store extra information about each user
class UserProfile(models.Model):
    
    # Define a set of roles that users can have
    ROLES_CHOICE = [
        ('counsellor', 'Counsellor'),
        ('hod', 'HOD'),
        ('accountant', 'Accountant'),
        ('principal', 'Principal')
    ]

    # Link this profile to Django's built-in User model (One-to-One relationship)
    # This means every User will have one and only one UserProfile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Store the role of the user — value must be one of the defined choices above
    role = models.CharField(max_length=20, choices=ROLES_CHOICE)

    # Optional field — some roles (like counsellors) may have a specific window number
    window_number = models.IntegerField(blank=True, null=True)
    
    # Define how this object will appear as a string (e.g., in admin panel or debug)
    def __str__(self):
        return f"{self.user.username} ({self.role})"
