# Generated by Django 3.2.7 on 2021-09-19 14:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Pagos', '0008_alter_pagos_numerofactura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 9, 19, 14, 32, 22, 681504, tzinfo=utc)),
        ),
    ]
