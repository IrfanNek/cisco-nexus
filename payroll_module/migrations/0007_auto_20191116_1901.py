# Generated by Django 2.2.5 on 2019-11-16 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_module', '0006_auto_20191116_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='pay_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 16, 19, 1, 59, 243077)),
        ),
    ]
