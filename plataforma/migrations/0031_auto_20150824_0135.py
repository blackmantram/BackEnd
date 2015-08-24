# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0030_auto_20150823_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuestionariorol',
            options={'ordering': ['orden']},
        ),
        migrations.AddField(
            model_name='cuestionariorol',
            name='orden',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
