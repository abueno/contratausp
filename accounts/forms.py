from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    # Increased max_length of username to acommodate e-mail addresses
    username = forms.CharField(label="Username", max_length=75)