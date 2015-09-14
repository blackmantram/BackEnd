# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0034_preguntassimilitud_similitud'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preguntassimilitud',
            old_name='pregunta_problema',
            new_name='pregunta_A',
        ),
        migrations.RenameField(
            model_name='preguntassimilitud',
            old_name='pregunta_solucion',
            new_name='pregunta_B',
        ),
        migrations.AlterField(
            model_name='preguntassimilitud',
            name='funcion',
            field=models.ForeignKey(to='plataforma.Similitud'),
            preserve_default=True,
        ),
    ]
