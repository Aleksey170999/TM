# Generated by Django 4.0.3 on 2022-04-09 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TM_app', '0005_alter_timesmodel_in_date_alter_timesmodel_out_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesmodel',
            name='pere',
        ),
        migrations.AlterField(
            model_name='timesmodel',
            name='in_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='timesmodel',
            name='out_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='timesmodel',
            name='user_name',
            field=models.CharField(default='123', max_length=50),
        ),
    ]
