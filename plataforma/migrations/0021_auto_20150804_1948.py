# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0020_auto_20150804_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipopregunta',
            name='cuestionario',
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='tipo_pregunta',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'U', b'UNICA RESPUESTA'), (b'M', b'MULTIPLE RESPUESTA'), (b'L', b'LISTA')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='TipoPregunta',
        ),
    ]
