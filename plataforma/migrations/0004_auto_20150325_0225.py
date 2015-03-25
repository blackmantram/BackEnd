# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_auto_20150325_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion_institucion',
            field=models.CharField(default=None, max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono_institucion',
            field=models.CharField(default=None, max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='ubicacion_institucion',
            field=models.CharField(default=None, max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
