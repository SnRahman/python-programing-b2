from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255)
    contact_no = models.CharField(max_length=15)


# make migrations 
# py manage.py makemigrations
# py manage.py migrate