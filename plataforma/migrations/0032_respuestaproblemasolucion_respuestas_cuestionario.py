# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0031_auto_20150824_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestaproblemasolucion',
            name='respuestas_cuestionario',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
