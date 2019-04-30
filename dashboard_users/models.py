from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Volunteer_details(models.Model):
    v_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    fullname = models.CharField(max_length=200)
    joined = models.DateField()
    center = models.CharField(max_length=200)
    contact = models.CharField(max_length=11,default='00000000000')

    class Meta:
        verbose_name_plural='Volunteer_details'
        
        
class Student_details(models.Model):
    volunteer=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    gender = models.CharField(max_length=6,choices=(('Male', 'Male'), ('Female', 'Female')), default='Male')
    class Meta:
        verbose_name_plural='Student_details'