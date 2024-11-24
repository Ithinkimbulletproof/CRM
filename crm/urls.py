from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("chat/", include("chat.urls")),
    path("employees/", include("employees.urls")),
    path("tasks/", include("tasks.urls")),
]
