# Generated by Django 4.0.3 on 2022-04-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_time', models.DateTimeField()),
                ('out_time', models.DateTimeField()),
            ],
        ),
    ]