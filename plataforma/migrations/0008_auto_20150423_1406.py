# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0007_auto_20150423_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='RespuestaProblemaSolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(null=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('tipo', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'PROBLEMA'), (b'S', b'SOLUCION')])),
                ('usuario', models.ForeignKey(to='plataforma.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='problemasolucion',
            name='categoria',
            field=models.ManyToManyField(to='plataforma.Categoria'),
            preserve_default=True,
        ),
    ]
