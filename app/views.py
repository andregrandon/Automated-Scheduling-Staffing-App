from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.http import HttpResponse
from django.contrib import messages
from .models import Employee

# Creates form and adds info to database
# def index(request):
#     form = EmployeeForm()
#
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#
#     context= {'form':form}
#     return render(request, 'index.html',context)


def index(request):
    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            First = form.cleaned_data['employee_first']
            First_name=First.capitalize()
            for object in Employee.objects.all():
                if object.employee_id == employee_id and object.employee_first== First_name:
                    messages.success(request,'ID is in database!')
                else:
                    messages.error(request,"not in database")
                    # return redirect(error_redirect)

    context= {'form':form}
    return render(request, 'index.html',context)





# def checkout(request):
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'The book has been checked out.')
#             return redirect('front-page')
#     else:
#         form = CheckoutForm()
#         return render(request, 'checkout/checkout.html', {'form': form})
#
# def error_redirect():
#
