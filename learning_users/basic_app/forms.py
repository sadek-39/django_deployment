from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from django.forms import ModelForm


class Userform(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','email','password']

#    form=Userform()

class UserProfileInfoForm(ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=['portfolio_site','profile_pic']
