from django import forms

class SignupForm(forms.Form):
    f_name = forms.CharField(max_length=100)
    l_name = forms.CharField(max_length=100,required=False)
    email = forms.EmailField()
    contact_no = forms.CharField(max_length=15)
