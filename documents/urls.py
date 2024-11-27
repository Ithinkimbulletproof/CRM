from django.urls import path
from . import views

urlpatterns = [
    path("", views.documents_view, name="documents"),
]
