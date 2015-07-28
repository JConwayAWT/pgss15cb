# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import skeletonpages.models


class Migration(migrations.Migration):

    dependencies = [
        ('skeletonpages', '0010_auto_20150727_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='algorithmrun',
            name='input_file',
            field=models.FileField(null=True, upload_to=skeletonpages.models.upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='algorithmrun',
            name='output_file',
            field=models.FileField(null=True, upload_to=skeletonpages.models.upload_path, blank=True),
        ),
    ]
