# Generated by Django 3.2.6 on 2021-08-23 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_postmodel_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='author',
        ),
    ]
