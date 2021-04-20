import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# user accounts ( user and profile section)


class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user_created = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Registered User',
                                        primary_key=True)
    dob = models.DateField(verbose_name="Date of Birth", blank=True, null=True)

# add the user column to profile
