from django import forms 
from .models import User
# creating a form  
class SignUp_form(forms.ModelForm):
    # specify the name of model to use 
    class Meta: 
        model =  User
        fields = "__all__"