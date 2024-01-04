from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Textarea


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

        widgets={
            'username':TextInput(attrs={'class':"form-control", 'id':"cname", 'placeholder':"Name *", }),
            'email':TextInput(attrs={'class':"form-control" ,'id':"cemail" ,'placeholder':"Email *" }),
            'password1':TextInput(attrs={'class':"form-control" ,'id':"password1" ,'placeholder':"password1 *"}),
            'password2':TextInput(attrs={ 'class':"form-control" ,'id':"password2" ,'placeholder':"password2 *"}),
        }

   
