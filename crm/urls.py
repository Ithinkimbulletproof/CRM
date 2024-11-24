from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # path('chat/', include('chat.urls')),
    # path('employees/', include('employees.urls')),
    # path('tasks/', include('tasks.urls')),
]
