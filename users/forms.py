from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): # argument tells us this function inherits from UserCreationForm
    email = forms.EmailField() # required=True by default

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # fields to be shown in form and in what order

class UserUpdateForm(forms.ModelForm): # ModelForm allows model to be converted to Django form automatically, instead of redundantly having to write new code to match what you want
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']