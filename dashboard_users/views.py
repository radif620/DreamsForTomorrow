from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def user_home(request):
    return render(request, 'dashboard_users/base.html')
