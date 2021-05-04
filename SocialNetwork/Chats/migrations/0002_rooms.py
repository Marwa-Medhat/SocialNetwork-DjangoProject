# Generated by Django 3.2 on 2021-05-04 02:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_member', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
                ('room_messages', models.ManyToManyField(related_name='messages', to='Chats.Chat')),
            ],
        ),
    ]
