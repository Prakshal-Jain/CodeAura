from django.urls import path, include

from .views import *

app_name = "home"

urlpatterns = [path("",HomePage.as_view(),name="home")
               ]