# Generated by Django 5.0.6 on 2024-07-05 12:45

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armiya', '0005_yangiliklar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sh_rivojlanish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Talablar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]
