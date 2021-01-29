from django.urls import path, include

from .views import *

app_name = "dashboard"

urlpatterns = [path("overview",Overview.as_view(),name="overview"),
               ]