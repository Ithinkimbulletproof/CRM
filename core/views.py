from datetime import date, timedelta
from django.shortcuts import render
from tasks.models import Task

def home(request):
    today = date.today()
    tomorrow = today + timedelta(days=1)

    tasks = Task.objects.filter(due_date__gte=today, due_date__lte=tomorrow)

    for task in tasks:
        if task.due_date == today:
            task.due_date_text = "сегодня"
        elif task.due_date == tomorrow:
            task.due_date_text = "завтра"
        else:
            task.due_date_text = task.due_date.strftime("%d.%m.%Y")

        task.due_time = task.due_date.strftime("%H:%M") if task.due_date else ""

    return render(request, "core/home.html", {"tasks": tasks})
