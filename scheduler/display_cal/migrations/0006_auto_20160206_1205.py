# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display_cal', '0005_course_codenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='building',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(default=b'', max_length=70),
        ),
        migrations.AlterField(
            model_name='course',
            name='room',
            field=models.CharField(default=b'', max_length=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='other',
            field=models.TextField(default=b''),
        ),
    ]
