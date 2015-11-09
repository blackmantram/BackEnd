# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0045_auto_20151108_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestaproblemasolucion',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
