from django.urls import path
from .views import ai_chat

urlpatterns = [
    path("chat/", ai_chat, name="ai-chat"),
]

