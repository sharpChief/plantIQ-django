# Generated by Django 4.1.7 on 2023-05-05 12:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0009_modeldetector_lastupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelAlertHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('processName', models.CharField(max_length=250)),
                ('detectorName', models.CharField(max_length=250)),
                ('anomalyValue', models.FloatField(default=None)),
                ('alertAt', models.DateTimeField(default=datetime.datetime(2023, 5, 5, 12, 15, 41, 99316))),
            ],
        ),
        migrations.AlterField(
            model_name='modeldetector',
            name='lastUpdate',
            field=models.CharField(default='None', max_length=250),
        ),
        migrations.CreateModel(
            name='ModelAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('anomalyValue', models.FloatField(default=None)),
                ('status', models.BooleanField(default=True)),
                ('detector', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='base_app.modeldetector')),
            ],
        ),
    ]
