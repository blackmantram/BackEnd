# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0029_auto_20150823_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuestionarioRol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'PROBLEMA'), (b'S', b'SOLUCION')])),
                ('cuestionario', models.ForeignKey(to='plataforma.Cuestionario')),
                ('rol', models.ForeignKey(to='plataforma.Rol')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rol',
            name='cuestionarios',
            field=models.ManyToManyField(to='plataforma.Cuestionario', through='plataforma.CuestionarioRol'),
            preserve_default=True,
        ),
    ]
