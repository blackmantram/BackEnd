# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0017_auto_20150712_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tags',
            field=models.ManyToManyField(to='plataforma.Tag'),
            preserve_default=True,
        ),
    ]
