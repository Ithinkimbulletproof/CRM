from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class EmployeeManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Логин обязателен")
        extra_fields.setdefault("is_active", True)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, **extra_fields)


class Employee(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Логин", max_length=50, unique=True)
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50, blank=True, null=True)
    position = models.CharField("Должность", max_length=100)
    phone_number = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Электронная почта", unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"
