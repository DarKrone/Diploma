# Generated by Django 5.0.4 on 2024-04-19 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_courses_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='courseId',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.courses'),
        ),
    ]
