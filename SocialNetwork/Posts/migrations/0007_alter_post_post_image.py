# Generated by Django 3.2 on 2021-05-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0006_auto_20210502_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]