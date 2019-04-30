from django.contrib import admin
from django.urls import path, include
from dashboard_users import views as user_views

urlpatterns=[
    path('',user_views.user_dash,name='user-dash'),
    path('student_details/',user_views.student_details,name='student-details'),
    path('student_add/',user_views.student_add, name='student-add'),
]