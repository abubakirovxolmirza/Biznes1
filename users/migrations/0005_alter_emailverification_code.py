# Generated by Django 5.0.6 on 2024-06-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_emailverification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]
