from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,null=True)
    email = models.EmailField()
    contact_no = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id} - {self.first_name} - {self.last_name} - {self.email} - {self.contact_no}'