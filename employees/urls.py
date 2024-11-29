from django.urls import path
from .views import employee_list, profile
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path("", employee_list, name="employee_list"),
    path("profile/", profile, name="profile"),
    path("password_change/", PasswordChangeView.as_view(
        template_name="employees/password_change.html",
        success_url="/profile/"
    ), name="password_change"),
]
