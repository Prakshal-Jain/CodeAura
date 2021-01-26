from django.urls import path, include

from .views import *

app_name = "home"

urlpatterns = [path("",HomePage.as_view(),name="home"),
               path("signUp",SignIn.as_view(),name="signUp"),
               path("login",Login.as_view(),name="login"),
               ]