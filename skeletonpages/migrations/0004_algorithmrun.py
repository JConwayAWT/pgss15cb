# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeletonpages', '0003_auto_20150711_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlgorithmRun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name=b'Name', blank=True)),
                ('description', models.CharField(max_length=2048, null=True, verbose_name=b'Description', blank=True)),
                ('input_file', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('user_profile', models.OneToOneField(to='skeletonpages.UserProfile')),
            ],
        ),
    ]
