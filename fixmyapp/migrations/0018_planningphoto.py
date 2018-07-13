# Generated by Django 2.0 on 2018-07-13 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixmyapp', '0017_auto_20180713_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanningPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('height', models.PositiveIntegerField()),
                ('width', models.PositiveSmallIntegerField()),
                ('src', models.ImageField(height_field='height', upload_to='photos', width_field='width')),
                ('planning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='fixmyapp.Planning')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
