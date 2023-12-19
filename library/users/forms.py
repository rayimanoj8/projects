from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
class UserRegistrationForm(UserCreationForm):
    email = models.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class CreateSuperUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser']