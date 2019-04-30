from .models import Volunteer_details
from django import forms


class VolunteerDetailsForm(forms.ModelForm):
    class Meta:
        model = Volunteer_details
        fields = ['fullname','joined']