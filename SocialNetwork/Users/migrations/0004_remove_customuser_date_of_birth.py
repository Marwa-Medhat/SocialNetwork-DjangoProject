# Generated by Django 3.2 on 2021-05-02 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_delete_userdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_of_birth',
        ),
    ]
