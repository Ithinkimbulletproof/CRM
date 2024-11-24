from django.shortcuts import render


def employees_view(request):
    return render(request, "employees/employees.html")
