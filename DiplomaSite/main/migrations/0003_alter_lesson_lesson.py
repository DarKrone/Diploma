# Generated by Django 5.0.4 on 2024-04-26 20:31

import django_quill.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_lesson_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson',
            field=django_quill.fields.QuillField(blank=True, default=None, verbose_name='Занятие'),
        ),
    ]
