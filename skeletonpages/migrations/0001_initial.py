# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_name', models.CharField(max_length=255, null=True, verbose_name=b'Object Name', blank=True)),
                ('object_description', models.CharField(max_length=255, null=True, verbose_name=b'Object Description', blank=True)),
                ('object_number', models.CharField(max_length=255, null=True, verbose_name=b'Object Number', blank=True)),
            ],
        ),
    ]
