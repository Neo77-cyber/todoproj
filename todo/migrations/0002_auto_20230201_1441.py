# Generated by Django 3.0.14 on 2023-02-01 14:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
