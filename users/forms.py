from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import User, profile
from django import forms


class regForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class userUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name', 'last_name', 'username', 'email']

class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']