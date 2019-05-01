from .models import Volunteer_details,Student_details,Task, TaskAssign
from django import forms
from django.contrib.auth import get_user_model


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

class TaskAddForm(forms.ModelForm):
    class Meta:
        model=Task
        fields= ['title','type','assign_date']

class TaskAssignForm(forms.ModelForm):
    # students=forms.ModelChoiceField(queryset=Student_details.objects.filter(volunteer=user_id))
    # tasks=forms.ModelChoiceField(queryset=Task.objects.filter(assigned_by__id=user_id))

    class Meta:
        model=TaskAssign
        fields=['student','task','student_work','score','completed']

    def __init__(self, *args, **kwargs):
        user=kwargs.pop('user',None)
        super(TaskAssignForm, self).__init__(*args,**kwargs)
        if user:
            self.fields['student'].queryset = Student_details.objects.filter(volunteer=user)
            self.fields['task'].queryset = Task.objects.filter(assigned_by=user)