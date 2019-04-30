from .models import Volunteer_details,Student_details
from django import forms


class VolunteerDetailsForm(forms.ModelForm):
    contact= forms.CharField( widget=forms.TextInput(attrs={'type':'number'}),required=True)
    class Meta:
        model = Volunteer_details
        fields = ['fullname','joined','contact']


class StudentAddForm(forms.ModelForm):
    birth_date=forms.DateInput()
    class Meta:
        model=Student_details
        fields = ['name','birth_date','gender']