# Generated by Django 4.0.3 on 2022-04-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TM_app', '0002_timesmodel_in_date_timesmodel_out_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesmodel',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
