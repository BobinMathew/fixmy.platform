# Generated by Django 2.0 on 2018-07-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixmyapp', '0020_auto_20180727_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='status',
            field=models.CharField(
                blank=True,
                choices=[
                    ('unknown', 'unknown'),
                    ('idea', 'idea'),
                    ('preliminary planning', 'preliminary planning'),
                    ('blueprint planning', 'blueprint planning'),
                    ('approval planning', 'approval planning'),
                    ('execution planning', 'execution planning'),
                    ('preparation of awarding', 'preparation of awarding'),
                    ('awarding', 'awarding'),
                    (
                        'execution of construction work',
                        'execution of construction work',
                    ),
                    ('ready', 'ready'),
                ],
                max_length=30,
                null=True,
            ),
        ),
    ]
