# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0037_auto_20150928_2043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pregunta',
            options={'ordering': ['orden']},
        ),
        migrations.AddField(
            model_name='pregunta',
            name='orden',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
