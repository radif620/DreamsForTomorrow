from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Volunteer_center(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    center = models.CharField(max_length=150, choices=(('DHK','Dhaka'),('SYL','Sylhet'),('CTG','Chittagong')),default='DHK')

@receiver(post_save,sender=User)
def create_vol_center(sender, instance, created, **kwargs):
    if created:
        Volunteer_center.objects.create(user=instance)

# @receiver(post_save,sender=User)
# def save_vol_center(sender,instance,**kwargs):
#     instance.volunteer_center.save()

