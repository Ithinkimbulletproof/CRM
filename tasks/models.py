from django.db import models
from django.utils.translation import gettext_lazy as _
from employees.models import Employee


class Task(models.Model):
    STATUS_CHOICES = [
        ("New", _("Новая")),
        ("In Progress", _("В процессе")),
        ("Completed", _("Выполнена")),
    ]

    title = models.CharField(max_length=255, verbose_name=_("Название задачи"))
    description = models.TextField(verbose_name=_("Описание задачи"), blank=True)
    due_date = models.DateField(
        verbose_name=_("Крайний срок (дата)"), blank=True, null=True
    )
    due_time = models.TimeField(
        verbose_name=_("Крайний срок (время)"), blank=True, null=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="New",
        verbose_name=_("Статус задачи"),
    )
    completed_at = models.DateTimeField(
        verbose_name=_("Дата завершения"), blank=True, null=True
    )
    creator = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="created_tasks",
        verbose_name=_("Создатель задачи"),
    )
    assignee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks",
        verbose_name=_("Исполнитель"),
    )

    def __str__(self):
        return self.title
