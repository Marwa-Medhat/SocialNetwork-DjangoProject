# Generated by Django 3.2 on 2021-05-04 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='Reciever',
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='Sender',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]
