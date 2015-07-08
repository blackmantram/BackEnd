# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0012_auto_20150625_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problemasolucion',
            old_name='categoria',
            new_name='categorias',
        ),
    ]
