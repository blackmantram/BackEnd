# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0028_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuestionariopregunta',
            name='dependencia_respuestas',
            field=models.ManyToManyField(to='plataforma.OpcionesDeRespuesta'),
        ),
    ]
