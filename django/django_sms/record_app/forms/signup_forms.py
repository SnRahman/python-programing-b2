from django import forms
from ..models import Student


# class StudentForm(forms.Form):
class StudentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255,required=False)
    email = forms.EmailField()
    contact_no = forms.CharField(max_length=30)

    class Meta:
        model = Student
        fields = ('__all__')