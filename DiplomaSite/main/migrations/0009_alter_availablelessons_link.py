# Generated by Django 5.0.4 on 2024-05-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_availablelessons_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablelessons',
            name='link',
            field=models.URLField(blank=True, default=None, max_length=250, verbose_name='Ссылка'),
        ),
    ]
