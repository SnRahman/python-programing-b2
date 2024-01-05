from django.shortcuts import render
from django.http import HttpResponse
from .forms.signup_form import SignupForm
from .forms.register_form import RegisterForm
from .models import Student



# Create your views here.
def index(request):
    return HttpResponse('index page')

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        # return HttpResponse(form)
        return render(request,'django_form.html',{'form': form})
    else:
        form_data = SignupForm( request.POST )

        if form_data.is_valid():
            f_name = form_data.cleaned_data.get('f_name')
            l_name = form_data.cleaned_data['l_name']
            email = form_data.cleaned_data.get('email')
            contact_no = form_data.cleaned_data.get('contact_no')

            student = Student(f_name = f_name, l_name= l_name, email=email , contact_no = contact_no)
            student.save()

            return HttpResponse('form is submitted')
        else:
            return HttpResponse("Invalid Form")
        
# insert data from forms to models directly
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        # return HttpResponse(form)
        return render(request,'django_form1.html',{'form': form})
    else:
        form_data = RegisterForm( request.POST )

        if form_data.is_valid():
            form_data.save()
            return HttpResponse('form is submitted')
        else:
            return HttpResponse("Invalid Form")
        