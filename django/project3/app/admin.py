from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email','contact_no')


# admin.site.register(Customer)
admin.site.register(Customer,CustomerAdmin)