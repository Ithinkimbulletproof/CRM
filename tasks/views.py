from django.shortcuts import render


def tasks_view(request):
    return render(request, "tasks/tasks.html")
