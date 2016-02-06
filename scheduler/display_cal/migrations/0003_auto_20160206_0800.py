# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display_cal', '0002_course_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('day', models.CharField(default=b'NA', max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='day',
        ),
        migrations.RemoveField(
            model_name='course',
            name='endTime',
        ),
        migrations.RemoveField(
            model_name='course',
            name='startTime',
        ),
        migrations.AddField(
            model_name='period',
            name='courses',
            field=models.ManyToManyField(to='display_cal.Course'),
        ),
    ]
