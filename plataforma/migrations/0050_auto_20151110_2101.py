# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0049_auto_20151110_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='visto',
            field=models.BooleanField(default=False),
        ),
    ]
