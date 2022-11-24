from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()


    context= {'form':form}
    return render(request, 'index.html',context)
