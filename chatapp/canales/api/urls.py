from django.urls import path
from canales.api.views import ChatList, ChatDetail, MensajeList, MensajePorChat, MensajePorChatYUsuario

urlpatterns = [
    path('chats/', ChatList.as_view(), name='chat-list'),
    path('chats/<int:pk>/', ChatDetail.as_view(), name='chat-detail'),
    path('mensajes/', MensajeList.as_view(), name='mensaje-list'),
    path('chats/<int:chat_id>/mensajes/', MensajePorChat.as_view(), name='mensaje-por-chat'),
    path('chats/<int:chat_id>/mensajes/<str:username>/', MensajePorChatYUsuario.as_view(), name='mensaje-por-chat-y-usuario'),
]