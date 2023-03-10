# Generated by Django 4.1.4 on 2022-12-27 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_creacion', models.CharField(max_length=50)),
                ('usuario_modificacion', models.CharField(max_length=50)),
                ('descripcion', models.CharField(help_text='Descripción de la categoría', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
