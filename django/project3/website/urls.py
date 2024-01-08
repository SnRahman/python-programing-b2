from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('register/',views.register,name='register'),
    path('edit/<int:id>', views.edit , name='edit'),
    path('delete/<int:id>', views.delete , name='delete'),
]