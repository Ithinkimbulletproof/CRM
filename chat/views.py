from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatRoom
from .forms import ChatRoomForm
import logging

logger = logging.getLogger("chat")


@login_required
def chat_list(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, "chat/chat_list.html", {"chat_rooms": chat_rooms})


@login_required
def chat_room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    return render(request, "chat/chat_room.html", {"room_name": room.name})


@login_required
def create_chat(request):
    if request.method == "POST":
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            try:
                chat_room = form.save(commit=False)
                chat_room.created_by = request.user
                chat_room.save()
                logger.debug(
                    f"Комната '{chat_room.name}' создана пользователем {request.user.username}."
                )
                return redirect("chat_list")
            except Exception as e:
                logger.error(f"Ошибка при создании комнаты: {e}")
        else:
            logger.warning(f"Форма создания комнаты содержит ошибки: {form.errors}")
    else:
        form = ChatRoomForm()
    return render(request, "chat/create_chat.html", {"form": form})


@login_required
def update_chat(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    if request.method == "POST":
        form = ChatRoomForm(request.POST, instance=room)
        if form.is_valid():
            try:
                form.save()
                logger.debug(f"Комната '{room.name}' успешно обновлена.")
                return redirect("chat_list")
            except Exception as e:
                logger.error(f"Ошибка при обновлении комнаты: {e}")
        else:
            logger.warning(f"Форма изменения комнаты содержит ошибки: {form.errors}")
    else:
        form = ChatRoomForm(instance=room)
    return render(request, "chat/update_chat.html", {"form": form, "room": room})


@login_required
def delete_chat(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    if request.method == "POST":
        room.delete()
        logger.debug(f"Комната '{room.name}' удалена.")
        return redirect("chat_list")
