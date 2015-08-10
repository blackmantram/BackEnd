# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0021_auto_20150804_1948'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsuarioOpcionRespuesta',
            new_name='ProblemaSolucionOpcionRespuesta',
        ),
        migrations.RemoveField(
            model_name='problemasolucionopcionrespuesta',
            name='usuario',
        ),
        migrations.AddField(
            model_name='problemasolucionopcionrespuesta',
            name='problema_solucion',
            field=models.ForeignKey(default=1, to='plataforma.ProblemaSolucion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='opcionesderespuesta',
            name='pregunta',
            field=models.ForeignKey(related_name='opciones', to='plataforma.Pregunta'),
            preserve_default=True,
        ),
    ]
