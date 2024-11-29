from django.contrib import admin
from .models import Employee
from .forms import EmployeeCreationForm


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "position",
        "phone_number",
        "email",
    )
    search_fields = ("username", "first_name", "last_name", "position", "email")
    list_filter = ("position",)

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            kwargs["form"] = EmployeeCreationForm
        return super().get_form(request, obj, **kwargs)
