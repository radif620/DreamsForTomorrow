from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Volunteer_details(models.Model):
    v_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    fullname = models.CharField(max_length=200)
    joined = models.DateField()
    center = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural='Volunteer_details'