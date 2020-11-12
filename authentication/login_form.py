from django.forms import ModelForm 
from django import forms 
from .models import *

class Loginform(ModelForm):
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email','password')

    
    def clean_password(self,*args,**keyargs):
        password = self.cleaned_data.get('password')

        if len(password)<=6:
            raise forms.ValidationError("input password is too short please enter correct one ")