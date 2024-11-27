from django import forms
from .models import Employee

class EmployeeCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        help_text="Введите пароль."
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput,
        help_text="Введите пароль ещё раз для проверки."
    )

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'phone_number', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        return password2

    def save(self, commit=True):
        employee = super().save(commit=False)
        employee.set_password(self.cleaned_data["password1"])
        if commit:
            employee.save()
        return employee
