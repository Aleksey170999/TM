# Generated by Django 4.0.3 on 2022-04-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TM_app', '0004_alter_timesmodel_pere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesmodel',
            name='in_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='timesmodel',
            name='out_date',
            field=models.DateField(),
        ),
    ]