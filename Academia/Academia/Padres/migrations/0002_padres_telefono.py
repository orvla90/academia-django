# Generated by Django 3.2.7 on 2021-09-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Padres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='padres',
            name='telefono',
            field=models.CharField(default=10, max_length=30),
            preserve_default=False,
        ),
    ]