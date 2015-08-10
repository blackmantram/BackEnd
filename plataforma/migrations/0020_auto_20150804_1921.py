# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0019_auto_20150804_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuestionarioPregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField()),
                ('cuestionario', models.ForeignKey(to='plataforma.Cuestionario')),
                ('dependencia_respuesta', models.ForeignKey(to='plataforma.OpcionesDeRespuesta', null=True)),
                ('pregunta', models.ForeignKey(to='plataforma.Pregunta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='preguntas',
            field=models.ManyToManyField(to='plataforma.Pregunta', through='plataforma.CuestionarioPregunta'),
            preserve_default=True,
        ),
    ]
