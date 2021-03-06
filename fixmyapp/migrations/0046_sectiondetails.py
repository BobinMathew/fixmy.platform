# Generated by Django 2.0.12 on 2019-09-20 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixmyapp', '0045_auto_20190918_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionDetails',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                (
                    'side',
                    models.PositiveSmallIntegerField(
                        choices=[(0, 'right'), (1, 'left')]
                    ),
                ),
                ('speed_limit', models.PositiveSmallIntegerField()),
                ('daily_traffic', models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    'daily_traffic_heavy',
                    models.DecimalField(decimal_places=2, max_digits=8),
                ),
                (
                    'daily_traffic_cargo',
                    models.DecimalField(decimal_places=2, max_digits=8),
                ),
                (
                    'daily_traffic_bus',
                    models.DecimalField(decimal_places=2, max_digits=8),
                ),
                ('length', models.DecimalField(decimal_places=2, max_digits=8)),
                ('crossings', models.PositiveSmallIntegerField()),
                (
                    'orientation',
                    models.CharField(
                        choices=[
                            ('N', 'north'),
                            ('E', 'east'),
                            ('S', 'south'),
                            ('W', 'west'),
                        ],
                        max_length=1,
                    ),
                ),
                ('rva1', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva2', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva3', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva4', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva5', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva6', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva7', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva8', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva9', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva10', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva11', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva12', models.DecimalField(decimal_places=12, max_digits=16)),
                ('rva13', models.DecimalField(decimal_places=12, max_digits=16)),
                (
                    'section',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='details',
                        to='fixmyapp.Section',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Section details',
                'verbose_name_plural': 'Section details',
            },
        ),
    ]
