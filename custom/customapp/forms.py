# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    # Add any additional fields or override methods if needed
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput)
