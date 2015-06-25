# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0008_auto_20150423_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestaproblemasolucion',
            name='titulo',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
