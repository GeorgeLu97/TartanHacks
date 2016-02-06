# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display_cal', '0004_person_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='codeNumber',
            field=models.CharField(default=b'', max_length=8),
        ),
    ]
