from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pgss15compbio.settings')

from django.conf import settings

app = Celery('pgss15compbio')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from skeletonpages.forms import AlgorithmRunForm
from django.core.urlresolvers import reverse
from skeletonpages.models import *
from Parser import Parser
from django.core.files import File
from time import time
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from random import random
import json
import pdb
from django.utils.safestring import mark_safe
import Parser
from StringIO import StringIO


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task(bind=True)
def add(self, a, b):
  return AlgorithmRun.objects.last().name

@app.task(bind = True)
def finish_iteration(self, new_algorithm_run_id):
  new_algorithm_run = AlgorithmRun.objects.get(pk = new_algorithm_run_id)
  file_name = "./pgss15compbio/media/out_file_{}.txt".format( str(random())[2:] )
  out_file = File(open(file_name, "w+"))
  p = Parser.Parser()
  model = p.get_model(new_algorithm_run.input_file, out_file)
  model.iterate()

  new_algorithm_run.status = "COMPLETE"
  new_algorithm_run.output_file = out_file
  new_algorithm_run.save()

  print "Complete"

  return 0
