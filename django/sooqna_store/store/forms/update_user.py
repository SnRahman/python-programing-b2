from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UpdateUser(UserChangeForm):


    class Meta:
        model = User
        fields = ('first_name','last_name','email')

    def __init__(self, *args, **wargs):
        super(UpdateUser,self).__init__(*args, **wargs)


        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'