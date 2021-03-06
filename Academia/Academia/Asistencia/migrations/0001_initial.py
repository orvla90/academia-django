# Generated by Django 3.2.7 on 2021-09-20 09:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alumnos', '0008_alter_alumnos_fechainscripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('horas', models.IntegerField(default=0)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumnos.alumnos')),
            ],
        ),
    ]
