# Generated by Django 4.0.3 on 2022-03-19 08:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_roompost_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterField(
            model_name='roompost',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
