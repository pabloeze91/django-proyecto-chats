from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(
        verbose_name='nombre', max_length=60, default=''
    )

    class Meta:
        db_table = 'chatapp_chat'
        verbose_name = 'chat'
        verbose_name_plural = 'chats'

    def __str__(self):
        return f'{self.id} - {self.nombre}'
    
class Mensaje(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    user = models.ForeignKey(
        User, verbose_name='user', on_delete=models.CASCADE,
    )
    chat = models.ForeignKey(
        Chat, verbose_name='chat', on_delete=models.CASCADE
    )
    contenido = models.CharField(
        verbose_name='contenido', max_length=300, default=''
    )
    creado = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = 'chatapp_mensaje'
        verbose_name = 'mensaje'
        verbose_name_plural = 'mensajes'

    def __str__(self):
        return f"{self.user} - {self.chat}: {self.contenido}"
