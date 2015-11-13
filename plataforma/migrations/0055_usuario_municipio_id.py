# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0054_variable'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='municipio_id',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
    ]
