from django.urls import path
from .views import employee_list, update_employee

urlpatterns = [
    path("", employee_list, name="employee_list"),
    path("<int:pk>/edit/", update_employee, name="edit_employee"),
]
