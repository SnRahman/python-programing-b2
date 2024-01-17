from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms.create_user import CreateUser

# Create your views here.
def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'GET':
        form = CreateUser()

        # form = UserCreationForm()
        # return HttpResponse(form)
        return render(request,'signup.html',{'form':form})
    else:
        form = CreateUser(request.POST)
        if form.is_valid:
            user = form.save()
            return HttpResponse('form submitted')


def login(request):
    return render(request,'login.html')