from django.shortcuts import render
from django.http import HttpResponse

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


