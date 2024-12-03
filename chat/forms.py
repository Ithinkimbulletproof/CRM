from django import forms
from .models import ChatRoom


class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ["name"]
        labels = {
            "name": "Название комнаты",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название комнаты",
                }
            ),
        }
