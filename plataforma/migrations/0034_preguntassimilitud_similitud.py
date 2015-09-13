# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0033_auto_20150927_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntasSimilitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('funcion', models.ForeignKey(to='plataforma.Pregunta')),
                ('pregunta_problema', models.ForeignKey(related_name='pregunta_problema', to='plataforma.Pregunta')),
                ('pregunta_solucion', models.ForeignKey(related_name='pregunta_solucion', to='plataforma.Pregunta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Similitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('funcion', models.CharField(max_length=50, null=True)),
                ('descripcion', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
