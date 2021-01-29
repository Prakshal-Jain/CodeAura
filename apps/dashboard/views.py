from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class Overview(TemplateView):
    template_name = "overview.html"