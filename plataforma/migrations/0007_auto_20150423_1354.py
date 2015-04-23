# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0006_auto_20150421_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('nivel', models.IntegerField(default=0)),
                ('categoria_padre', models.ForeignKey(to='plataforma.Categoria', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='problemasolucion',
            name='tipo',
            field=models.CharField(default=b'P', max_length=1, choices=[(b'P', b'PROBLEMA'), (b'S', b'SOLUCION')]),
            preserve_default=True,
        ),
    ]
