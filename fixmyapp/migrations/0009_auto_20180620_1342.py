# Generated by Django 2.0 on 2018-06-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixmyapp', '0008_auto_20180620_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='category_of_bike',
            field=models.CharField(
                blank=True,
                choices=[
                    ('racing_cycle', 'racing cycle'),
                    ('city_bike', 'city bike'),
                    ('mountain_bike', 'mountain bike'),
                    ('e_bike', 'e-bike'),
                    ('cargo_bike', 'cargo bike'),
                    ('e_cargo_bike', 'e-cargo-bike'),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(
                blank=True,
                choices=[('m', 'male'), ('f', 'female'), ('o', 'other')],
                max_length=1,
                null=True,
            ),
        ),
    ]
