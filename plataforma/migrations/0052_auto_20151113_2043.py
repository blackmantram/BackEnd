# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0051_mensaje_conversacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='conversacion',
            field=models.ForeignKey(related_name='mensajes', to='plataforma.Conversacion'),
        ),
    ]
