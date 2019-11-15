# Generated by Django 2.2.5 on 2019-11-06 14:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_module', '0017_auto_20191106_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shiftstatus',
            options={'verbose_name': 'Shift Status', 'verbose_name_plural': 'Shift Statuses'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 22, 40, 19, 322938)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 22, 40, 19, 322908)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance_module.Guard'),
        ),
    ]
