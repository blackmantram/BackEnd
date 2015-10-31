# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0042_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestaproblemasolucion',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='respuestaproblemasolucion',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='respuestaproblemasolucion',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='respuestaproblemasolucion',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='respuestaproblemasolucion',
            name='usuario',
        ),
        migrations.AddField(
            model_name='respuestaproblemasolucion',
            name='busqueda',
            field=models.ForeignKey(related_name='busqueda', default=1, to='plataforma.ProblemaSolucion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuestaproblemasolucion',
            name='respuesta',
            field=models.ForeignKey(related_name='respuesta', default=1, to='plataforma.ProblemaSolucion'),
            preserve_default=False,
        ),
    ]
