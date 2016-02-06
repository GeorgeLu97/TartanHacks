# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('building', models.CharField(max_length=20)),
                ('room', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('other', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='people',
            field=models.ManyToManyField(to='display_cal.Person'),
        ),
    ]
