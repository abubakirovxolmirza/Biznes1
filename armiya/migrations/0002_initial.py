# Generated by Django 5.0.6 on 2024-05-27 14:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('armiya', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='armiya_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historytasks',
            name='tasks_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armiya.tasks'),
        ),
    ]