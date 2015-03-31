# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0002_usuario_correo_institucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='descripcion',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rol',
            name='imagen',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='NIT',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo_institucion',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion_institucion',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_institucion',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono_institucion',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ubicacion_institucion',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
