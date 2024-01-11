from django import forms
from ..models import Employee

class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget= forms.TextInput(attrs={'class':'form-control'}) )
    last_name = forms.CharField(max_length=50,required=False)
    email = forms.EmailField()
    contact_no = forms.CharField(max_length=11)
    profile_img = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = Employee
        fields = ('__all__')
