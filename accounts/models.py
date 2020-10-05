from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(
        max_length=30, blank=True, null=True, help_text="Optional.")
    last_name = models.CharField(
        max_length=30,  blank=True, null=True, help_text="Optional.")
    email = models.EmailField(
        max_length=254, help_text="Required. Inform a valid email address")
    address = models.TextField(max_length=500, blank=True)
