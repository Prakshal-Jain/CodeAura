from django.shortcuts import render
from .models import Team
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.http import HttpResponse

# Create your views here.

class HomePage(TemplateView):
    template_name = "home/home_page.html"
    def get_context_data(self, *args, **kwargs):
        lis = super().get_context_data()
        lis["team_lis"] = Team.objects.all()
        return lis

class TeamView(ListView):
    template_name = 'home/team.html'
