from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.models import Volunteer_center
from dashboard_admin.forms import VolunteerCenterForm


# Create your views here.

def admin_home(request):
    return render(request, 'dashboard_admin/base.html')


def register_volunteer(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST,instance=request.user)
        # form = UserForm(request.POST, instance=request.user)
        form_vol_cen = VolunteerCenterForm(request.POST)
        if form.is_valid() and form_vol_cen.is_valid():
            form.save()
            form_vol_cen.save()
            return redirect('admin-home')  # to redirect to page after form is submitted

    else:
        form = UserCreationForm(instance=request.user)
        form_vol_cen = VolunteerCenterForm(request.POST)

    return render(request, 'dashboard_admin/vol_acc_form.html', {'form': form,'form_vol_cen' : form_vol_cen})
