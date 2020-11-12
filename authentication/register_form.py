from django.forms import ModelForm 
from django import forms 
from .models import *

class Registerform(ModelForm):
    password=forms.CharField(min_length=6 ,widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','email','password','confirm_password')

    
    def clean_confirm_password(self,*args,**keyargs):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm_password')
        if password!=confirm:
            raise forms.ValidationError('password not mached')


