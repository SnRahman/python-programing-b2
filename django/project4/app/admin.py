from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','contact_no')

# Register your models here.
# admin.site.register(Employee)
admin.site.register(Employee,EmployeeAdmin)