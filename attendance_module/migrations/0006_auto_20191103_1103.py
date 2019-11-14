# Generated by Django 2.2.5 on 2019-11-03 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_module', '0005_auto_20191022_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['start_datetime'], 'verbose_name_plural': 'Entries'},
        ),
        migrations.RemoveField(
            model_name='entry',
            name='date',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='hours_worked',
        ),
        migrations.AddField(
            model_name='entry',
            name='end_datetime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='start_datetime',
            field=models.DateField(default=datetime.datetime(2019, 11, 3, 11, 3, 51, 285509)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
