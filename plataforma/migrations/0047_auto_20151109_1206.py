# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0046_auto_20151108_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestaproblemasolucion',
            name='respuesta',
            field=models.ForeignKey(related_name='respuesta', to='plataforma.ProblemaSolucion', null=True),
        ),
    ]
