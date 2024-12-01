from datetime import timedelta, time
from django.shortcuts import render
from django.utils.timezone import localdate
from tasks.models import Task
from django.db.models import Q, Value
from django.db.models.functions import Coalesce
import logging

logger = logging.getLogger("tasks")

def home(request):
    today = localdate()
    tomorrow = today + timedelta(days=1)

    logger.debug(f"Сегодняшняя дата: {today}, Завтрашняя дата: {tomorrow}")

    tasks = Task.objects.filter(
        Q(creator=request.user) | Q(assignee=request.user),
        due_date__gte=today,
        due_date__lte=tomorrow,
    ).annotate(
        sort_time=Coalesce('due_time', Value(time.max))
    ).order_by('due_date', 'sort_time')

    logger.debug(f"Найдено задач: {tasks.count()}")

    for task in tasks:
        logger.debug(f"Обработка задачи: {task.title} (ID: {task.id}, Дата выполнения: {task.due_date}, Время: {task.due_time})")
        if task.due_date == today:
            task.due_date_text = "сегодня"
        elif task.due_date == tomorrow:
            task.due_date_text = "завтра"
        else:
            task.due_date_text = task.due_date.strftime("%d.%m.%Y")

    logger.debug(f"Отправлено задач на рендеринг: {[task.title for task in tasks]}")

    return render(request, "core/home.html", {"tasks": tasks})
