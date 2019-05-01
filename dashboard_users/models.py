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

    def __str__(self):
        return self.name


class Task(models.Model):
    assigned_by=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    type=models.CharField(max_length=150,choices=(('Individual','Individual'),('Group','Group')),default='Individual')
    assign_date=models.DateField()

    def __str__(self):
        return self.title


class TaskAssign(models.Model):
    student = models.ForeignKey(Student_details,on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student_work = models.TextField()
    completed = models.BooleanField()
    score = models.IntegerField()

    class Meta:
        unique_together=('student','task')

