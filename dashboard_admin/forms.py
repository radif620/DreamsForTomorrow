from django.forms import ModelForm
from django import forms
from users.models import Volunteer_center
from django.contrib.auth.models import User

class VolunteerCenterForm(forms.ModelForm):
    class Meta:
        model = Volunteer_center
        fields = ['center']
#
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
