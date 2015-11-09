# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0044_problemasolucion_respuestas_asociadas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemasolucion',
            name='respuestas_asociadas',
        ),
        migrations.AddField(
            model_name='respuestaproblemasolucion',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='respuestaproblemasolucion',
            name='fecha',
            field=models.DateTimeField(default='2005-01-01', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuestaproblemasolucion',
            name='tipo',
            field=models.CharField(default=b'P', max_length=1, choices=[(b'P', b'PROBLEMA'), (b'S', b'SOLUCION')]),
        ),
        migrations.AddField(
            model_name='respuestaproblemasolucion',
            name='titulo',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
