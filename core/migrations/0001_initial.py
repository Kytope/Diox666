# Generated by Django 5.0 on 2024-10-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('numero_identificacion', models.CharField(max_length=20, unique=True)),
                ('contacto_emergencia', models.CharField(max_length=100)),
                ('telefono_emergencia', models.CharField(max_length=20)),
            ],
        ),
    ]
