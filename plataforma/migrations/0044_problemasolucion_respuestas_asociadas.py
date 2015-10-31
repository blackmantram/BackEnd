# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0043_auto_20151031_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemasolucion',
            name='respuestas_asociadas',
            field=models.ManyToManyField(to='plataforma.ProblemaSolucion', through='plataforma.RespuestaProblemaSolucion'),
        ),
    ]
