# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0005_auto_20150421_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemasolucion',
            name='descripcion',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
