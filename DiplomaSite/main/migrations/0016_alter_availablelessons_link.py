# Generated by Django 5.0.4 on 2024-05-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_availablelessons_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablelessons',
            name='link',
            field=models.URLField(default='http://127.0.0.1:8000/availablelesson/', max_length=250, verbose_name='Ссылка'),
        ),
    ]