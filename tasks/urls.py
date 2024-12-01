from django.urls import path
from .views import create_task, tasks_view, update_task, delete_task, tasks_history

urlpatterns = [
    path("", tasks_view, name="tasks"),
    path("create/", create_task, name="create_task"),
    path("update/<int:task_id>/", update_task, name="update_task"),
    path("delete/<int:task_id>/", delete_task, name="delete_task"),
    path("task_history/", tasks_history, name="tasks_history"),
]
