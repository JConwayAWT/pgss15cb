# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeletonpages', '0006_auto_20150723_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithmrun',
            name='input_text',
            field=models.CharField(max_length=8192, null=True, verbose_name=b'Input Text', blank=True),
        ),
        migrations.AddField(
            model_name='algorithmrun',
            name='output_text',
            field=models.CharField(max_length=32768, null=True, verbose_name=b'Output Text', blank=True),
        ),
    ]
