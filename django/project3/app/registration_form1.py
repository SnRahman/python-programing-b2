from django import forms

class RegistrationForm1(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200,required=False)
    email = forms.EmailField()
    contact_no = forms.CharField(max_length=11)