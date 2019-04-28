from django.shortcuts import render


# Create your views here.
def user_check(request):
    if request.user.is_staff:
        return render(request, 'dashboard_admin/base.html')
    else:
        return render(request, 'dashboard_users/base.html')
