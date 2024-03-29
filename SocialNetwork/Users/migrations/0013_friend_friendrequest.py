# Generated by Django 3.2 on 2021-05-06 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0012_merge_20210506_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('send', 'send'), ('accepted', 'accepted'), ('cancel', 'cancel')], default=None, max_length=8)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recieverRequest', to=settings.AUTH_USER_MODEL)),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senderRequest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userfriend', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
