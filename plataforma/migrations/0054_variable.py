# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0053_rol_tipo_rol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('variable', models.CharField(max_length=200)),
                ('valor', models.IntegerField()),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
    ]
