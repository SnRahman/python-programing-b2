from django.shortcuts import render
from django.http import HttpResponse

from .forms.employee_form import EmployeeForm


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
    