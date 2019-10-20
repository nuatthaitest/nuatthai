from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import datetime


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    birthday = forms.DateField(input_formats='%m/%d/%y',required=False)

    mobile = forms.CharField(max_length=12,min_length=12,initial="+63")

    class Meta:
        model = User
        fields = ['first_name', 'last_name','birthday', 'email','mobile', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
