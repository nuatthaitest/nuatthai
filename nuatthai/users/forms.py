from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Services
import datetime


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    birthday = forms.DateField(input_formats='%m/%d/%y',required=False)

    mobile = forms.IntegerField(initial = "09",min_value=900000000)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','birthday', 'username','email','mobile', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class ServiceForm(forms.ModelForm):
    CHOICES = (
        (350, 'Nuat Thai Foot Massage(1hour)'),
        (350, 'Thai Body massage w/ Oil(1hour)'),
        (400, 'Sweddish Massage(1hour)'),
        (400, 'Armoatherapy Massage(1hour)'),
        (250, 'Express - Back and Head(30 mins)'),
        (250, 'Foot Massage(30 mins)'),
        (250, 'Back Massage(30 mins)'),
        (250, 'Head massage(30 mins)'),
    )

    service = forms.ChoiceField(required = True, choices = CHOICES, widget=forms.RadioSelect(attrs={'class' : 'Radio'}), initial={'regular_service':'Regular Service'})

    class Meta:
        model = User
        fields = ['service']
