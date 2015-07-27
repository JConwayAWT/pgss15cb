# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeletonpages', '0005_auto_20150720_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithmrun',
            name='output_file',
            field=models.FileField(null=True, upload_to=b'documents/output/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='algorithmrun',
            name='input_file',
            field=models.FileField(null=True, upload_to=b'documents/%Y/%m/%d', blank=True),
        ),
    ]
