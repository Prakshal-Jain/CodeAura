from django.db import models
from datetime import date
from django import forms
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.utils import timezone
from django.core.exceptions import ValidationError


# TODO: add image deletion after an update or delete of a model

# Create your models here.
class Team(models.Model):
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    profile_image = models.ImageField(null=False, blank=True, upload_to="Team_profile_media")
    comments = models.TextField("What do you think about CodeAura?", max_length=200)
    contribution = models.CharField("Please enter your contributions.", max_length=100, default="Contributor")
    email = models.EmailField("Email", default="codeaurahelpdesk@gmail.com")
    join_date = models.DateTimeField("Date joined", default=timezone.now)

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField("Email Address", unique=True)
    username = models.CharField(max_length=100)

    is_staff = models.BooleanField(
        "is staff",
        default=False,
        help_text="Admin site access",
    )

    is_active = models.BooleanField(
        "User active",
        default=True,
        null=True,
        help_text="if a user is active."
    )

    date_joined = models.DateTimeField("Date joined", default=timezone.now)

    REQUIRED_FIELDS = ("first_name", "last_name", "username")

    class Meta:
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return self.username

    def clean(self):
        for required_field in self.REQUIRED_FIELDS:
            if getattr(self, required_field) is None:
                raise ValidationError(f"Field '{required_field}' is missing.")

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, models.CASCADE, related_name="profile"
    )
    display_picture = models.ImageField()
    date_of_birth = models.DateField()

    REQUIRED_FIELDS = ("date_of_birth",)

    def clean(self):
        for required_field in self.REQUIRED_FIELDS:
            if getattr(self, required_field) is None:
                raise ValidationError(f"Field '{required_field}' is missing.")

