from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Profile(models.Model):
    # Fix: change 'on_url' to 'on_delete'
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                 on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
class User(AbstractUser):
    # This allows us to extend the user later with 'bio' or 'social_id'
    pass
