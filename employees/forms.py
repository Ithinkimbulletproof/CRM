from django import forms
from .models import Employee


class EmployeeCreationForm(forms.ModelForm):
    username = forms.CharField(
        label="Логин",
        max_length=50,
        help_text="Введите уникальный логин для сотрудника.",
        disabled=True,
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput, help_text="Введите пароль."
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput,
        help_text="Введите пароль ещё раз для проверки.",
    )

    class Meta:
        model = Employee
        fields = [
            "username",
            "first_name",
            "last_name",
            "middle_name",
            "position",
            "phone_number",
            "email",
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if Employee.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким логином уже существует.")
        return username

    def save(self, commit=True):
        employee = super().save(commit=False)
        if self.cleaned_data.get("password1"):
            employee.set_password(self.cleaned_data["password1"])
        if commit:
            employee.save()
        return employee
