# Generated by Django 5.0.2 on 2024-04-24 21:14

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='code',
            field=tinymce.models.HTMLField(),
        ),
    ]
