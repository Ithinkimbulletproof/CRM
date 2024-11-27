from django.db import models
from django.contrib.auth.hashers import make_password

class Employee(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    position = models.CharField("Должность", max_length=100)
    phone_number = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Электронная почта", unique=True, blank=True, null=True)
    password = models.CharField("Пароль", max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"
