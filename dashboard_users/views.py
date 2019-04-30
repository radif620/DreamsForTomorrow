from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from users.models import Volunteer_center
from .forms import VolunteerDetailsForm, StudentAddForm
from .models import Volunteer_details, Student_details
from django.views.generic import ListView
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
        return render(request, 'dashboard_users/home.html',context)

def volunteer_profile(request):
    form = VolunteerDetailsForm(request.POST or None)
    if form.is_valid():
        center = Volunteer_center.objects.filter(user__username=str(request.user.username))[0].center
        print(center)
        print(form.cleaned_data)
        fullname = form.cleaned_data['fullname']
        joined = form.cleaned_data['joined']
        contact = form.cleaned_data['contact']
        obj = Volunteer_details.objects.create(v_id=request.user,fullname=fullname,joined=joined,center=center,contact=contact)
        print(obj)
        return redirect('user-dash')  

    template_name = 'dashboard_users/volunteer_details.html'
    context = {
        'form': form
    }

    return render(request, template_name, context)

def student_add(request):
    form = StudentAddForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        dob = form.cleaned_data['birth_date']
        gender = form.cleaned_data['gender']
        obj = Student_details.objects.create(volunteer=request.user,name=name,birth_date=dob,gender=gender)
        print(obj)
        form = StudentAddForm()
        redirect('student-add')

    context= {'form' : form}
    template_name='dashboard_users/student_add.html'
    return render(request,template_name,context)


def student_details(request):
    try:
        students=Student_details.objects.filter(volunteer__id=request.user.id)
        # students = Student_details.objects.get(volunteer=request.user)
    except:
        students = None

    print(students)
    context={'students': students}
    return render(request,'dashboard_users/student_details.html',context)

class studentlistview(ListView):
    model = Student_details
    context_object_name = 'students'
    template_name = 'dashboard_users/student_details.html'
    ordering = ['name']
