# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0009_auto_20150625_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tag', models.CharField(max_length=255)),
                ('problema_solucion', models.ManyToManyField(to='plataforma.ProblemaSolucion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
