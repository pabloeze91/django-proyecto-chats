# Generated by Django 3.2.2 on 2024-10-07 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=60, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'chat',
                'verbose_name_plural': 'chats',
                'db_table': 'chatapp_chat',
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('contenido', models.CharField(default='', max_length=300, verbose_name='contenido')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canales.chat', verbose_name='chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'mensaje',
                'verbose_name_plural': 'mensajes',
                'db_table': 'chatapp_mensaje',
            },
        ),
    ]
