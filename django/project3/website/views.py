from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q


from .forms.signup_form import SignupForm
from .forms.register_form import RegisterForm
from .models import Student




# Create your views here.
def index(request):
    # get all data form model
    students = Student.objects.all()

    # get total records
    # total = Student.objects.count()
    # total = students.count()
    # return HttpResponse(total)


    # get data by any key
    # students = Student.objects.get(id=5)
    # students = Student.objects.get(pk=4)

    # get multiple records by columns names
    # students = Student.objects.filter(f_name='ahmad')
    # students = Student.objects.filter(email='admin@admin.com')

    # get data using multiple columns at once
    # students = Student.objects.filter(f_name='mohsin' ,l_name='Ali')
    # students = Student.objects.get(f_name='mohsin' ,l_name='Ali')






    # get data using or gates 
    # students = Student.objects.filter( Q(f_name='mohsin') | Q(l_name='usman') )



    # return HttpResponse(students)
    return render(request,'students.html', {'students' : students })

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
        form_data = RegisterForm( request.POST, request.FILES )
        
        if form_data.is_valid():
            # img = form_data.cleaned_data['profile_img']
            form_data.save()
            return HttpResponse('form is submitted')
        else:
            return HttpResponse("Invalid Form")
        

def delete(request,id):
    student = Student.objects.get(id=id)
    # student.delete()
    return redirect( index )
    # return HttpResponse(f'Student record deleted: {id}')

def edit(request,id):

    student = Student.objects.get(id=id)
    student.f_name = 'Adeel'
    student.l_name = 'Ahmad'
    student.email = 'adeelahmad@gmail.com'
    student.contact_no = '031324871257'
    student.save()

    return HttpResponse(student)
    return HttpResponse(f'Edit Route: {id}')