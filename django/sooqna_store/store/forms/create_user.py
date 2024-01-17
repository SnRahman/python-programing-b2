from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUser(UserCreationForm):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={ 'placeholder': 'First Name', 'class': 'form-inputs'}))
    last_name = forms.CharField(max_length=150,required=True , widget=forms.TextInput(attrs={ 'placeholder': 'Last Name', 'class': 'form-inputs'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={ 'placeholder': 'Email', 'class': 'form-inputs'}))


    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')

    
    def __init__(self,*args,**kwargs):
        super(CreateUser,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].widget.attrs['class'] = 'form-inputs'


        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-inputs'

        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'form-inputs'