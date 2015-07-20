# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeletonpages', '0004_algorithmrun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithmrun',
            name='user_profile',
            field=models.OneToOneField(null=True, to='skeletonpages.UserProfile'),
        ),
    ]
