from datetime import timedelta, time
from django.shortcuts import render
from django.utils.timezone import localtime
from tasks.models import Task
from django.db.models import Q, Value
from django.db.models.functions import Coalesce
import logging

logger = logging.getLogger("tasks")


def home(request):
    now = localtime()
    today = now.date()
    tomorrow = today + timedelta(days=1)

    evening_time = time(15, 0)
    is_evening = now.time() >= evening_time

    logger.debug(
        f"Текущее время: {now}, Сегодняшняя дата: {today}, Завтрашняя дата: {tomorrow}, Вечер после {evening_time}: {is_evening}"
    )

    tasks = (
        Task.objects.filter(
            Q(creator=request.user) | Q(assignee=request.user),
            (
                Q(due_date=today, due_time__gte=now.time())
                | Q(due_date=tomorrow, due_time__lte=time.max)
                if is_evening
                else Q(due_date=today)
            ),
        )
        .annotate(sort_time=Coalesce("due_time", Value(time.max)))
        .order_by("due_date", "sort_time")
    )

    logger.debug(f"Найдено задач: {tasks.count()}")

    for task in tasks:
        logger.debug(
            f"Обработка задачи: {task.title} (ID: {task.id}, Дата выполнения: {task.due_date}, Время: {task.due_time})"
        )
        if task.due_date == today:
            task.due_date_text = "сегодня"
        elif task.due_date == tomorrow:
            task.due_date_text = "завтра"
        else:
            task.due_date_text = task.due_date.strftime("%d.%m.%Y")

    logger.debug(f"Отправлено задач на рендеринг: {[task.title for task in tasks]}")

    return render(request, "core/home.html", {"tasks": tasks})
