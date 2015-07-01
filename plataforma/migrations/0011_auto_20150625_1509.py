# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0010_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='problema_solucion',
        ),
        migrations.AddField(
            model_name='problemasolucion',
            name='tag',
            field=models.ManyToManyField(to='plataforma.Tag'),
            preserve_default=True,
        ),
    ]
