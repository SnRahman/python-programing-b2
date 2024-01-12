from django.shortcuts import render
from django.http import HttpResponse
from .forms.employee_form import EmployeeForm

# user auth forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms.user_creation_form import UserCreationCustomForm
from .forms.user_edit_form import UserChangeCustomForm

# user auth model
from django.contrib.auth.models import User

def dashboard(request):
    users = User.objects.all()
    return render(request,'dashboard.html',{'users':users})
    # return HttpResponse(users)



def signup(request):
    if request.method == 'GET':
        # form = UserCreationForm()
        form = UserCreationCustomForm()

        # return HttpResponse(form)
        return render(request,'signup.html',{'form':form})
    else:
        form = UserCreationCustomForm(request.POST)

        if form.is_valid :
            form.save()
            return HttpResponse('user Created')
        else:
            return HttpResponse('Invalid info')



def edit_user(request,id):
    user = User.objects.get(id=id)

    if request.method == 'GET':
        form = UserChangeCustomForm(request.POST or None,instance=user)
        return render(request,'edit_user.html',{'form':form,'user_id':id} )

        # form = UserChangeForm()
        # return HttpResponse(form)
        # return HttpResponse(f'edit: {id}')
    else:
        form = UserChangeCustomForm(request.POST,instance=user)

        if form.is_valid:
            form.save()
            return HttpResponse('Record updated')
        else:
            return HttpResponse('invalid data')

def delete_user(request,id):
    return HttpResponse(f'delete: {id}')

# Create your views here.
def register(request):
    if request.method == 'GET':
        form = EmployeeForm()
        # return HttpResponse('hello') 
        return render(request,'django_form.html',{'form':form})
    else:
        form = EmployeeForm(request.POST,request.FILES)

        if form.is_valid:
            form.save()
            return HttpResponse('form is submitted')         
        else:
            return HttpResponse('Invalid data')         
        return HttpResponse()
    