# Generated by Django 2.0 on 2018-07-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixmyapp', '0016_auto_20180713_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='cross_section_photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
