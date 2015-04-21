# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_problemasolucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemasolucion',
            name='usuario',
            field=models.ForeignKey(default=1, to='plataforma.Usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problemasolucion',
            name='descripcion',
            field=models.TextField(default=None),
            preserve_default=True,
        ),
    ]
