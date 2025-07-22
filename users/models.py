from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class UserProfile(models.Model):
    ROLES_CHOICE = [
        ('counsellor', 'Counsellor'),
        ('hod', 'HOD'),
        ('accountant', 'Accountant'),
        ('principal', 'Principal')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES_CHOICE)
    window_number = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} ({self.role})"