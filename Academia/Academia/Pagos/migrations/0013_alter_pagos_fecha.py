# Generated by Django 3.2.7 on 2021-09-20 09:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Pagos', '0012_alter_pagos_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 9, 20, 9, 43, 3, 805140, tzinfo=utc)),
        ),
    ]