# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeletonpages', '0007_auto_20150723_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='algorithmrun',
            name='user_profile',
        ),
    ]
