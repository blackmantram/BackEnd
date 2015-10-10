# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0039_auto_20151010_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcionesderespuesta',
            name='valor',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
