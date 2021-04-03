from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomerUserManager

# Create your models here.


class UserProfile(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    email = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(null=True, blank=True, auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    objects = CustomerUserManager()

    def __str__(self):
        return self.email
