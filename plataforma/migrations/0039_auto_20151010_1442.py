# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0038_auto_20151003_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pregunta',
            options={},
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='orden',
        ),
    ]
