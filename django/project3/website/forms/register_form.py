from django import forms
from ..models import Student

class RegisterForm(forms.ModelForm):
    f_name = forms.CharField(max_length=100)
    l_name = forms.CharField(max_length=100,required=False)
    email = forms.EmailField()
    contact_no = forms.CharField(max_length=15)

    class Meta:
        model = Student
        # fields = ['f_name', 'l_name','email','contact_no']
        fields = ('__all__')
        # exclude = ('id')
