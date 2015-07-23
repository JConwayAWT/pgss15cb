# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeletonpages', '0008_remove_algorithmrun_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='algorithm_runs',
            field=models.ManyToManyField(to='skeletonpages.AlgorithmRun'),
        ),
    ]
