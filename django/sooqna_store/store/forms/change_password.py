from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class ChangePassword(PasswordChangeForm):


    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')


    def __init__(self,*args, **kwargs):
        super(ChangePassword,self).__init__(*args, **kwargs)


        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'