# Generated by Django 4.0.3 on 2022-03-19 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_alter_message_options_alter_roompost_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roompost',
            name='img_url',
        ),
    ]
