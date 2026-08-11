from django import forms

# Django automatically handles the user creation form and model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Make a new model form for the registration so that we can add new fields to the django base form
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
