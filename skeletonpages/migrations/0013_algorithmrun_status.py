# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeletonpages', '0012_remove_userprofile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithmrun',
            name='status',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Status', blank=True),
        ),
    ]
