# Generated by Django 2.2.10 on 2020-03-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixmyapp', '0061_remove_report_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='description'),
        ),
    ]
