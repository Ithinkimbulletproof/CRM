from django.db import models
from employees.models import Employee


class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In Progress', 'В процессе'),
        ('Completed', 'Выполнена'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание задачи", blank=True)
    due_date = models.DateField(verbose_name="Крайний срок", blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='New', verbose_name="Статус задачи")
    creator = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="created_tasks",
                                verbose_name="Создатель задачи")
    assignee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="assigned_tasks", verbose_name="Исполнитель")

    def __str__(self):
        return self.title
