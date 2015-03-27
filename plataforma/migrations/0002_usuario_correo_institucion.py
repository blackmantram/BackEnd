# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo_institucion',
            field=models.CharField(default=None, max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
