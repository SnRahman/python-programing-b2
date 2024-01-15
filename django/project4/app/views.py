from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms.employee_form import EmployeeForm

# user authentication
from django.contrib.auth import authenticate, login, logout

# user auth forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms.user_creation_form import UserCreationCustomForm
from .forms.user_edit_form import UserChangeCustomForm

# user auth model
from django.contrib.auth.models import User

# flash messages
from django.contrib import messages

def dashboard(request):
    # return HttpResponse(request.user.is_authenticated)
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request,'dashboard.html',{'users':users})
    else:
        messages.error(request,'Kindly Login first')
        return redirect('login')
    # return HttpResponse(users)


def user_logout(request):
    logout(request)
    messages.success(request,'Logout successfully!')
    return redirect('login')


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
            messages.success(request,'User Created Successfully!')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid info')
            return redirect('signup')


def user_login(request):
    if request.method == 'POST':
        # return HttpResponse(request.POST)
        email = request.POST['email']
        password = request.POST['password']

        if email and password:
            user = authenticate(request,username=email, password=password)
            if user is not None:
                login(request,user)

                # set flash messages
                messages.success(request,'Login successfully!')
                
                return redirect('dashboard')
                # return HttpResponse(user)
            else:
                messages.error(request,'User not found')
                return redirect('signup')
    else:
        return render(request,'login.html')


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
            messages.success(request,'Record updated Successfully!')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid data')
            return redirect('edit_user',id)

def delete_user(request,id):
    user = User.objects.get(id=id)
    user.delete()

    messages.success(request,'User deleted Successfully!')
    return redirect('dashboard')

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
    