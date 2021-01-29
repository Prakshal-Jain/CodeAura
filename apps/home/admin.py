from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Team, User, UserProfile

# Register your models here.
admin.site.register(Team)

@admin.register(User)
class UserAdmin(UserAdmin):

    inlines = (
        UserProfile,
    )