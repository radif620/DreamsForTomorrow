from django.shortcuts import render,redirect
from dashboard_users.models import Volunteer_details


# Create your views here.
def user_check(request):
    if request.user.is_staff:
        return render(request, 'dashboard_admin/base.html')
    else:
        try:
            obj = Volunteer_details.objects.get(request.user.id)
        except:
            obj=None

        if obj is None:
            return redirect('/user_dash/')
        else:
            return render(request, 'dashboard_users/base.html')