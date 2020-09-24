from django import forms
from .models import RegistrationData

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'Username'
                               }))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={
                                   'class':'form-control',
                                   'placeholder':'Password'
                               }))
    email = forms.CharField(max_length=100,
                            widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'placeholder':'Enter Password'
                            }))
    phone = forms.CharField(max_length=100,
                            widget=forms.NumberInput(attrs={
                                'class':'form-control',
                                'placeholder':'Phone'
                            }))
