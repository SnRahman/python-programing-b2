from django.urls import path
from . import views

urlpatterns = [ 
    path('home/',views.home),
    path('about/',views.about),
    path('shop/',views.shop),
    # path('details/<id>',views.details)
    path('details/<int:id>',views.details,name='details'),
    path('registrtion_form/',views.registrtion_form,name='registrtion_form'),
    path('register/',views.register,name='register')

]