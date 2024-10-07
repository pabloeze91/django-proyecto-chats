from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import get_object_or_404
from canales.models import Chat, Mensaje
from canales.api.serializers import ChatSerializer, MensajeSerializer
from rest_framework.permissions import IsAuthenticated


class ChatList(APIView):
    def get(self, request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            chat = serializer.save()
            return Response(ChatSerializer(chat).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChatDetail(APIView):
    def get(self, request, pk):
        chat = get_object_or_404(Chat, pk=pk)
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    def patch(self, request, pk):
        chat = get_object_or_404(Chat, pk=pk)
        serializer = ChatSerializer(chat, data=request.data)
        if serializer.is_valid():
            chat = serializer.save()
            return Response(ChatSerializer(chat).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MensajePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class MensajeList(APIView):
    pagination_class = MensajePagination
    permission_classes = [IsAuthenticated]


    def get(self, request):
        mensajes = Mensaje.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(mensajes, request)
        serializer = MensajeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MensajePorChat(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, chat_id):
        mensajes = Mensaje.objects.filter(chat_id=chat_id)
        if not mensajes.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MensajeSerializer(mensajes, many=True)
        return Response(serializer.data)

class MensajePorChatYUsuario(APIView):
    def get(self, request, chat_id, username):
        mensajes = Mensaje.objects.filter(chat_id=chat_id, user__username=username)
        if not mensajes.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MensajeSerializer(mensajes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
