# Generated by Django 5.0.4 on 2024-04-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_task_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Номер урока'),
            preserve_default=False,
        ),
    ]
