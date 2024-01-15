from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('',views.dashboard,name='dashboard'),
    path('edit/<int:id>/',views.edit_user,name='edit_user'),
    path('delete/<int:id>/',views.delete_user,name='delete_user'),
    
]
