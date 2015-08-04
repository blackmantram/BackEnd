# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0018_usuario_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, null=True)),
                ('descripcion', models.TextField(null=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpcionesDeRespuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=200, null=True)),
                ('orden', models.IntegerField()),
                ('valor', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enunciado', models.CharField(max_length=200, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoPregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, null=True)),
                ('cuestionario', models.ForeignKey(to='plataforma.Cuestionario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsuarioOpcionRespuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opcion_respuesta', models.ForeignKey(to='plataforma.OpcionesDeRespuesta')),
                ('usuario', models.ForeignKey(to='plataforma.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tipo_pregunta',
            field=models.ForeignKey(to='plataforma.TipoPregunta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='opcionesderespuesta',
            name='pregunta',
            field=models.ForeignKey(to='plataforma.Pregunta'),
            preserve_default=True,
        ),
    ]
