# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display_cal', '0003_auto_20160206_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
