from django.shortcuts import render
from .models import Team
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.http import HttpResponse
from .forms import SignUp_form

# Create your views here.

class HomePage(TemplateView):
    template_name = "home/home_page.html"
    def get_context_data(self, *args, **kwargs):
        lis = super().get_context_data()
        lis["team_lis"] = Team.objects.all()
        return lis

class TeamView(ListView):
    template_name = 'home/team.html'

class SignIn(TemplateView):
    template_name = "signups\sign-up.html"

class Login(TemplateView):
    template_name = "signups\login.html"

def home_view(request): 
    context ={} 
  
    # create object of form 
    form = SignUp_form(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        # save the form data to model 
        form.save() 
  
    context['form']= form 
    return render(request, "./templates/signups/login.html", context)