# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('icono', models.CharField(default=None, max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=200)),
                ('apellido1', models.CharField(max_length=200)),
                ('apellido2', models.CharField(max_length=200)),
                ('numero_documento', models.CharField(max_length=200)),
                ('correo', models.CharField(default=None, max_length=200, blank=True)),
                ('nombre_institucion', models.CharField(default=None, max_length=200, blank=True)),
                ('telefono_institucion', models.CharField(default=None, max_length=200, blank=True)),
                ('ubicacion_institucion', models.CharField(default=None, max_length=200, blank=True)),
                ('direccion_institucion', models.CharField(default=None, max_length=200, blank=True)),
                ('NIT', models.CharField(default=None, max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsuarioRedes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=200)),
                ('red_social', models.ForeignKey(to='plataforma.RedSocial')),
                ('usuario', models.ForeignKey(to='plataforma.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='usuario',
            name='redes',
            field=models.ManyToManyField(to='plataforma.RedSocial', through='plataforma.UsuarioRedes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(to='plataforma.Rol'),
            preserve_default=True,
        ),
    ]
