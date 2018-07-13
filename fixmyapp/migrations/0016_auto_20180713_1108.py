# Generated by Django 2.0 on 2018-07-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixmyapp', '0015_auto_20180713_0601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planning',
            old_name='url',
            new_name='external_url',
        ),
        migrations.AlterField(
            model_name='planning',
            name='planning_sections',
            field=models.ManyToManyField(related_name='plannings', to='fixmyapp.PlanningSection'),
        ),
    ]
