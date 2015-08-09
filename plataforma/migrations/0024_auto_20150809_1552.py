# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0023_auto_20150809_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuestionariopregunta',
            old_name='dependencia_respuesta',
            new_name='dependencia_respuestas',
        ),
    ]
