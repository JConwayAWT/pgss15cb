# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeletonpages', '0009_userprofile_algorithm_runs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='algorithm_runs',
            field=models.ManyToManyField(to='skeletonpages.AlgorithmRun', null=True, blank=True),
        ),
    ]
