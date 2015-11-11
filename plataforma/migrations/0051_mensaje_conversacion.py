# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0050_auto_20151110_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='conversacion',
            field=models.ForeignKey(default=8, to='plataforma.Conversacion'),
            preserve_default=False,
        ),
    ]
