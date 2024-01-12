from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class UserCreationCustomForm(UserCreationForm):
    first_name = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'} ))
    last_name = forms.CharField(max_length=150, required=False , widget=forms.TextInput( attrs={'class':'form-control'} ))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')


    def __init__(self, *args, **kwargs):
        super(UserCreationCustomForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

