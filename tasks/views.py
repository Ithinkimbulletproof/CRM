from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def tasks_view(request):
    tasks = Task.objects.filter(creator=request.user)
    return render(request, "tasks/tasks.html", {'tasks': tasks})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html', {'form': form})

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/update_task.html", {"form": form, "task": task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks/delete_task.html", {"task": task})

def tasks_history(request):
    completed_tasks = Task.objects.filter(status='Completed')

    return render(request, 'tasks/tasks_history.html', {'completed_tasks': completed_tasks})
