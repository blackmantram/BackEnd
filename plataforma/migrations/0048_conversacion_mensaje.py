# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0047_auto_20151109_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('busqueda', models.ForeignKey(related_name='busqueda_', to='plataforma.ProblemaSolucion')),
                ('respuesta', models.ForeignKey(related_name='respuesta_', to='plataforma.ProblemaSolucion', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensaje', models.TextField(null=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('conversacion', models.ForeignKey(to='plataforma.Conversacion')),
            ],
        ),
    ]
