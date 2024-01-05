from django.db import models

# Create your models here.
class Student(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255,null=True)
    email = models.EmailField()
    contact_no = models.CharField(max_length=30)

    def __str__(self):
        return f' {self.id} -  {self.f_name} - {self.l_name} - {self.email} - {self.contact_no}' 
