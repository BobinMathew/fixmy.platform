# Generated by Django 2.0 on 2018-05-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixmyapp', '0002_auto_20180419_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='planningsection',
            name='progress',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]