from django.contrib import admin

# Register your models here.
from canales.models import *

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ('nombre',)
    list_filter = ('nombre',)

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'chat', 'contenido', 'creado')
    list_display_links = ('contenido',)
    list_filter = ('user', 'chat', 'creado')
    search_fields = ('contenido',)