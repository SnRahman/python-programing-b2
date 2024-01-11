from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150 ,null=True)
    email = models.EmailField(max_length=150)
    contact_no = models.CharField(max_length=150)
    profile_img = models.ImageField(upload_to='app/profile_imgs')

    