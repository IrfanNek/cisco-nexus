# Generated by Django 2.2.5 on 2019-11-03 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_module', '0012_auto_20191103_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 3, 11, 23, 32, 610519)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 3, 11, 23, 32, 610489)),
        ),
    ]
