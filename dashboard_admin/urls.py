from django.urls import path
from . import views as admin_views

urlpatterns = [
    path('', admin_views.admin_home, name='admin-home'),
    path('register/', admin_views.register_volunteer, name='register-vol'),
]
