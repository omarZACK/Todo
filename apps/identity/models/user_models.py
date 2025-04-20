from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from Helpers.structure.models import TrackingModel as Tm
from apps.identity.models.enums import GenderChoices as Gender
from apps.identity.models.managers import UserManager
from Helpers.services.AvatarDrawer import generate_profile_image as gpi

class User(AbstractBaseUser, PermissionsMixin,Tm):
    """
    Custom user model that supports email-based authentication.
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE,null=True, blank=True)
    profile_picture_url = models.URLField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.profile_picture_url:
            letter = self.name[0]
            image_path = gpi(letter,self.email.__str__())
            self.profile_picture_url = image_path
        super().save(*args, **kwargs)