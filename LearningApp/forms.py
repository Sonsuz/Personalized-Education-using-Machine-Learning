from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserProfile
import datetime
from django.contrib.auth.forms import UserChangeForm









class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
         model = User
         fields = ['username', 'email','first_name', 'last_name']

class UserProfileForm(forms.ModelForm):

    class Meta:
         model = UserProfile
         fields = ['lan_ID','title', 'phone','image']
# Edit Profile ------------------------------------
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )
