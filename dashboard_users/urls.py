from django.contrib import admin
from django.urls import path, include
from dashboard_users import views as user_views

urlpatterns=[
    path('',user_views.user_dash,name='user-dash')
]