# Generated by Django 3.2 on 2021-05-04 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2021, 5, 4)),
        ),
    ]
