from django.contrib import admin
from .models import Volunteer_details,Student_details
# Register your models here.

admin.site.register(Volunteer_details,verbose_name_plural='Volunteer_details')
admin.site.register(Student_details)