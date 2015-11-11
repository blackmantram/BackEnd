# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0048_conversacion_mensaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='conversacion',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='destinatario',
            field=models.ForeignKey(related_name='usuario_destinatario', to='plataforma.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='usuario_busqueda',
            field=models.ForeignKey(related_name='usuario_busqueda', to='plataforma.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='usuario_respuesta',
            field=models.ForeignKey(related_name='usuario_respuesta', to='plataforma.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='visto',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
