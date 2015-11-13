# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0052_auto_20151113_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='tipo_rol',
            field=models.CharField(default=b'BC', max_length=2, choices=[(b'BC', b'Busca en comercio'), (b'BT', b'Turismo'), (b'O', b'Ofrece')]),
        ),
    ]
