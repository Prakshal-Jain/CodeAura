from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def default_view(request):
    return render(request,"core/default.html")




