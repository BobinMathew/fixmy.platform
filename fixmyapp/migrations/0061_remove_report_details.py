# Generated by Django 2.2.10 on 2020-03-08 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixmyapp', '0060_auto_20200308_0901'),
    ]

    operations = [
        migrations.RemoveField(model_name='report', name='details',),
    ]
