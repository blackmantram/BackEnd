# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0011_auto_20150625_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problemasolucion',
            old_name='tag',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='Tag',
            new_name='tag',
        ),
    ]
