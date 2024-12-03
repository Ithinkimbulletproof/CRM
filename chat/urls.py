from django.urls import path
from .views import chat_room, chat_list, create_chat, delete_chat, update_chat

urlpatterns = [
    path("", chat_list, name="chat_list"),
    path("create/", create_chat, name="create_chat"),
    path("<str:room_name>/", chat_room, name="chat_room"),
    path("<str:room_name>/update/", update_chat, name="update_chat"),
    path("<str:room_name>/delete/", delete_chat, name="delete_chat"),
]
