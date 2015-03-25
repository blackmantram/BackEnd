# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0002_auto_20150319_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='NIT',
            field=models.CharField(default=None, max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.CharField(default=None, max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre_institucion',
            field=models.CharField(default=None, max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
