from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee


def employee_list(request):
    employees = Employee.objects.filter(is_superuser=False)
    return render(request, "employees/employee_list.html", {"employees": employees})


@login_required
def profile(request):
    return render(request, "employees/profile.html")
