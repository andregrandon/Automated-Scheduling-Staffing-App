from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields=['employee_id','employee_first','employee_last','employee_shift',
        'email','phone']
