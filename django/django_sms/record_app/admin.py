from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','contact_no')

# Register your models here.
admin.site.register(Student,StudentAdmin)