from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_first", "employee_last",'employee_id','employee_shift',
    'email','phone','senority','status')

admin.site.unregister(Employee)
admin.site.register(Employee, EmployeeAdmin)
