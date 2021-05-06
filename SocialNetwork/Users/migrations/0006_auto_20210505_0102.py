# Generated by Django 3.2 on 2021-05-05 01:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_alter_customuser_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2021, 5, 5)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_avatar',
            field=models.ImageField(default='default.png', max_length=50, upload_to='media/'),
        ),
    ]
