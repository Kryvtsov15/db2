from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    born = forms.DateField()
    country = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'born', 'country', 'city', 'password1', 'password2', )