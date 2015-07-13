# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0013_auto_20150708_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='descripcion',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
