from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms.create_user import CreateUser
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):

    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        messages.warning(request,'kindly login first!.')
        return redirect('login')

def signup(request):
    if request.method == 'GET':
        form = CreateUser()

        # form = UserCreationForm()
        # return HttpResponse(form)
        return render(request,'signup.html',{'form':form})
    else:
        form = CreateUser(request.POST)
        try:
            if form.is_valid:
                user = form.save()
                messages.success(request,'User Registered Successfully!')
                return redirect('login')
                # return HttpResponse('form submitted')
            else:
                messages.error(request,'Invlaid Information.')
                return redirect('signup')
        except:
            messages.error(request,'Invlaid Information.')
            return redirect('signup')


def user_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST['username']
        user_password = request.POST['password']

        if username and user_password:
            user = authenticate(request,username=username, password=user_password)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged In successfully!')
                return redirect('home')
            else:
                messages.warning(request,"Username or Password is incorrect")
                return redirect('login')
        else:
            messages.warning(request,"Username and Password are required.")
            return redirect('login')
            # return HttpResponse(user)
        # return HttpResponse(request.POST)

def user_logout(request):
    logout(request) 
    messages.success(request,"You have been logged out successfully!")
    return redirect('login')

def edit_profile(request):
    return render(request,'edit_profile.html')