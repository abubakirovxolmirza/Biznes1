# Generated by Django 5.0.6 on 2024-07-09 13:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armiya', '0006_sh_rivojlanish_talablar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sh_rivojlanish',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='talablar',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='yangiliklar',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]