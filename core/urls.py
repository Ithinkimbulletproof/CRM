from django.contrib.auth import views as auth_views
from django.urls import path
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login, name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
