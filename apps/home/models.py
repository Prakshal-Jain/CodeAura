from django.db import models
from datetime import date

# Create your models here.
class Team(models.Model):
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    profile_image = models.ImageField(null=False, blank=True, upload_to="Team_profile_media")
    comments = models.TextField("What do you think about CodeAura?", max_length=200)
    contribution = models.CharField("Please enter your contributions.", max_length=100, default="Contributor")
    email = models.EmailField("Email", default="codeaurahelpdesk@gmail.com")
    join_date = date.today()