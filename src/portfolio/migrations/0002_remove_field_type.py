# Generated by Django 4.1.10 on 2023-10-01 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='type',
        ),
    ]
