# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0028_cuestionariopregunta_dependencia_respuestas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuestionariopregunta',
            options={'ordering': ['orden']},
        ),
        migrations.AlterModelOptions(
            name='opcionesderespuesta',
            options={'ordering': ['orden']},
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='imagen',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pregunta',
            name='imagen',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
