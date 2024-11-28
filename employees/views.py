from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeCreationForm

def employee_list(request):
    employees = Employee.objects.filter(is_superuser=False)
    return render(request, "employees/employee_list.html", {"employees": employees})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeCreationForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeCreationForm(instance=employee)
    return render(request, "employees/update_employee.html", {"form": form, "employee": employee})
