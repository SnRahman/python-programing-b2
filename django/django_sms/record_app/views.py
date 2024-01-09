from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms.signup_forms import StudentForm 
# from .forms.signup_form import StudentForm

# Create your views here.
def home(request):
    # return HttpResponse('Welcome!')
    students = Student.objects.all()
    # return HttpResponse(students) 
    return render(request,'records.html',{'students':students})


def signup(request):
    if request.method == 'GET':
        form = StudentForm()
        return render(request,'signup.html',{'form':form})
    else:
        # return HttpResponse(request.POST)
        form = StudentForm(request.POST or None)
        if form.is_valid():
            # form.cleaned_data['first_name']
            form.save()
            return redirect(home)
        
def edit(request,id):
    student = Student.objects.get(id=id)

    if request.method == 'GET':
        # return HttpResponse(student)
        form = StudentForm(request.POST or None, instance=student)
        return render(request,'edit_record.html',{'form':form ,'student':student})
    else:
        form = StudentForm(request.POST or None, instance=student)
        if form.is_valid():
            # form.cleaned_data['first_name']
            form.save()
            return redirect(home)
    # return HttpResponse(f'edit: {id}')

        
def delete(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(home)
    