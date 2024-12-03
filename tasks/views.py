from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.timezone import now
from .forms import TaskForm
from .models import Task
import logging

logger = logging.getLogger("tasks")


@login_required
def tasks_view(request):
    tasks = Task.objects.filter(Q(creator=request.user) | Q(assignee=request.user))
    tasks = tasks.exclude(status="Completed")
    tasks = tasks.order_by("due_date")

    my_tasks = tasks.filter(assignee=request.user)

    assigned_tasks = tasks.filter(creator=request.user).exclude(assignee=request.user)

    return render(
        request,
        "tasks/tasks.html",
        {
            "my_tasks": my_tasks,
            "assigned_tasks": assigned_tasks,
            "employee": request.user,
        },
    )


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                task = form.save(commit=False)
                task.creator = request.user
                task.save()
                logger.debug(
                    f"Задача '{task.title}' создана пользователем {request.user.username}."
                )
                return redirect("tasks")
            except Exception as e:
                logger.error(f"Ошибка при создании задачи: {e}")
        else:
            logger.warning(f"Форма создания задачи содержит ошибки: {form.errors}")
    else:
        logger.debug("Открыта страница создания задачи.")
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form})


@login_required
def update_task(request, task_id):
    logger.debug(f"Начата обработка изменения задачи с ID {task_id}.")
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            try:
                form.save()
                logger.debug(f"Задача '{task.title}' успешно обновлена.")
                return redirect("tasks")
            except Exception as e:
                logger.error(f"Ошибка при обновлении задачи: {e}")
        else:
            logger.warning(f"Форма изменения задачи содержит ошибки: {form.errors}")
    else:
        logger.debug(f"Загружена форма изменения задачи '{task.title}'.")
        form = TaskForm(instance=task)
    return render(request, "tasks/update_task.html", {"form": form, "task": task})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")
    return render(request, "tasks/delete_task.html", {"task": task})


@login_required
def detail_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST" and "mark_completed" in request.POST:
        task.status = "Completed"
        task.completed_at = now()
        task.save()
        return redirect("tasks_history")

    return render(request, "tasks/detail_task.html", {"task": task})


@login_required
def tasks_history(request):
    completed_tasks = Task.objects.filter(
        (Q(creator=request.user) | Q(assignee=request.user)) & Q(status="Completed")
    ).order_by("-completed_at")

    return render(
        request, "tasks/tasks_history.html", {"completed_tasks": completed_tasks}
    )
