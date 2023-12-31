from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms.registration_form import RegistrationForm 
from .registration_form1 import RegistrationForm1
from .models import Customer


# Create your views here.
def home(request):
    return HttpResponse('Hello World!')

def about(request):
    return HttpResponse('About page')

def shop(request):
    # return HttpResponse('Shop page')
    return render(request,'shop.html')

def details(request,id):
    # return HttpResponse(f'Details page: {id}')
    products = [
        {
            'id':'001',
            'name' : 'Sooper Buscuit',
            'price' : 50.00
        },
        {
            'id':'002',
            'name' : 'Tuc Buscuit',
            'price' : 55.00
        },
        {
            'id':'003',
            'name' : 'Dairy Milk Chocholate',
            'price' : 200.00
        },
        {
            'id':'004',
            'name' : 'Mars',
            'price' : 250.00
        }
    ]
    return render(request,'details.html',{ 'details_id' :id, 'username': '', 'products': products })


def registrtion_form(request):
    # form = RegistrationForm()
    form = RegistrationForm1()
    # return HttpResponse(form)
    # return render(request,'forms.html')
    return render(request,'django_forms.html',{'form':form})

def register(request):
    if request.method == 'POST':

        form_data = RegistrationForm1( request.POST )

        if form_data.is_valid():
            forms_data = request.POST
            f_name = forms_data['first_name']
            l_name = forms_data['last_name']
            email = forms_data['email']
            contact_no = forms_data['contact_no']

            customer =  Customer(first_name = f_name, last_name = l_name, email =email,contact_no = contact_no )
            customer.save()

            return HttpResponse(f'fist_name: {request.POST['first_name']} -- Last Name :{forms_data['last_name']} -- Email: {forms_data['email' ]} -- Contact No #: {forms_data['contact_no']}')
        else:
            return HttpResponse('Invalid inputs')
        
       

        # if first_name and last_name and email and contact_no:
        #     # return HttpResponse(forms_data)
        #     return HttpResponse(f'fist_name: {request.POST['first_name']} -- Last Name :{forms_data['last_name']} -- Email: {forms_data['email' ]} -- Contact No #: {forms_data['contact_no']}')
        # else:
        #     return HttpResponse('Invalid inputs')
    else:
        return redirect(registrtion_form)
        # return HttpResponse('Method not allowed')