# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display_cal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='day',
            field=models.CharField(default=b'NA', max_length=2),
        ),
    ]
