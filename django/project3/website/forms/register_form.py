from django import forms
from ..models import Student

class RegisterForm(forms.ModelForm):
    f_name = forms.CharField(
        max_length=100,
        widget= forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'First Name' 
            })
        )
    
    l_name = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'  }) )
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    contact_no = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Contact #'}))
    profile_img = forms.ImageField( widget=forms.FileInput(attrs= {'class':'form-control'}) )
    
    
    class Meta:
        model = Student
        # fields = ['f_name', 'l_name','email','contact_no']
        fields = ('__all__')
        # exclude = ('id')
