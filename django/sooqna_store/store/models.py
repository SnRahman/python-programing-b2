from django.db import models

class Category(models.Model):
    name = models.CharField(max_length= 255)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='store/products')
    category = models.ForeignKey(Category,on_delete = models.CASCADE)