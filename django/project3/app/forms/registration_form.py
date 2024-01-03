
from django import forms
class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200,required=False)
    email = forms.EmailField()
    contact_no = forms.CharField(max_length=11)

# from django.forms import Form, CharField, EmailField
# class RegistrationForm(Form):
#     first_name = CharField(max_length=200)
#     last_name = CharField(max_length=200,required=False)
#     email = EmailField()
#     contact_no = CharField(max_length=11)