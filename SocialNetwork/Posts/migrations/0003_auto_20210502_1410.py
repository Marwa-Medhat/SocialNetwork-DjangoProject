# Generated by Django 3.2 on 2021-05-02 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_alter_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 14, 10, 30, 326118)),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 14, 10, 30, 325588)),
        ),
    ]