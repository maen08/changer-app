from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.


class ChangerUser(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=True)
    is_changer_provider = models.BooleanField(default=False)  # the user which gives change
    is_change_seeker = models.BooleanField(default=False)  # the user who request change


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

