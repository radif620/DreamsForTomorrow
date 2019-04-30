from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Volunteer_center
from .forms import VolunteerDetailsForm
from .models import Volunteer_details
from django.http import HttpResponseRedirect
from django.shortcuts import redirect,get_object_or_404

# Create your views here.
@login_required
def user_dash(request):
    try:
        obj = Volunteer_details.objects.get(v_id=request.user.id)
    except Volunteer_details.DoesNotExist:
        obj=None       
    
    if obj is None:
        return volunteer_profile(request)        
    else:
        context={
            'name': obj.fullname,
            'center': obj.center,
            'joined': obj.joined
        }
        return render(request, 'dashboard_users/base.html',context)

def volunteer_profile(request):
    form = VolunteerDetailsForm(request.POST or None)
    if form.is_valid():
        center = Volunteer_center.objects.filter(user__username=str(request.user.username))[0].center
        print(center)
        print(form.cleaned_data)
        fullname = form.cleaned_data['fullname']
        joined = form.cleaned_data['joined']
        obj = Volunteer_details.objects.create(v_id=request.user,fullname=fullname,joined=joined,center=center)
        print(obj)   
        return redirect('user-dash')  

    template_name = 'dashboard_users/volunteer_details.html'
    context = {
        'form': form
    }

    return render(request, template_name, context)
