# Generated by Django 2.0.12 on 2019-09-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixmyapp', '0042_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
