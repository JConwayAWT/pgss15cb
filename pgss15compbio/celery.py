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
from Reagent import Reagent
from Reaction import Reaction


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

# def get_model(f, outFile):
#         """Returns a model for a given input file

#         f: input .react file name
#         """
#         states = {}
#         section_title=""
#         reactions = []
#         reaction_file = f
#         output_reagents = []
#         for line in reaction_file:
#             line = line.rstrip()
#             # print line
#             if line.startswith("#") or line == "":
#                 continue
#             elif line.startswith("["):
#                 section_title = line
#             elif '[Iterations' in section_title:
#                 num_iterations = int(float(line.strip()))
#                 if num_iterations <= 0:
#                     raise ValueError("Number of iterations must be positive")
#             elif '[Reagents' in section_title:
#                 name, count = line.split(':')
#                 name = name.strip()
#                 count = int(float(count.strip()))
#                 if count < 0:
#                     raise ValueError("Count can't be negative: " + line)
#                 states[name] = Reagent(count, name)
#             elif '[Reactions' in section_title:
#                 reaction, k = line.split("|")
#                 k = float(k)
#                 reactant_str, product_str = reaction.split("->")
#                 reactants = []
#                 products = []
#                 if "$" not in reactant_str:
#                     for reactant in reactant_str.split("+"):
#                         reactant = reactant.strip()
#                         if reactant[0].isalpha():
#                             reactant = "1" + reactant
#                         for i in xrange(len(reactant)):
#                             if reactant[i].isalpha():
#                                 coeff = -int(float(reactant[:i]))
#                                 if coeff >= 0: 
#                                     raise ValueError(
#                                         "Coefficient must be positive: " + \
#                                                                         line)
#                                 reactants.append((reactant[i:], coeff))
#                                 break
#                 if "$" not in product_str:
#                     for product in product_str.split("+"):
#                         product = product.strip()
#                         if product[0].isalpha():
#                             product = "1" + product
#                         for i in xrange(len(product)):
#                             if product[i].isalpha():
#                                 coeff = int(float(product[:i]))
#                                 if coeff <= 0:
#                                     raise ValueError(
#                                         "Coefficient must be positive: " + \
#                                                                         line)
#                                 products.append((product[i:], coeff))
#                                 break
#                 reactions.append(Reaction(states, reactants + products, k))
#             elif '[Output_Reagents' in section_title:
#                 output_reagents.append(line.strip())
#             elif "[Output_Frequency" in section_title:
#                 output_frequency = int(float(line.strip()))
#                 if output_frequency <= 0:
#                     raise ValueError("Output frequency must be positive")
#             elif "[RNG_Seed" in section_title:
#                 rng_seed = line.strip()
#                 if rng_seed != "r":
#                     rng_seed = int(float(rng_seed))
#                     if rng_seed <= 0:
#                         raise ValueError("RNG seed must be positive")
#                 else:
#                     rng_seed = -1
#             else:
#                 raise ValueError("Bad File")
#         for reaction in reactions:
#             for reagent in reaction.react_form_data:
#                 if reagent[0] not in states:
#                     raise ValueError("Reagent {} not defined".format(
#                                      reagent[0]))
#         for reagent in output_reagents:
#             if reagent not in states:
#                raise ValueError("Ouput Reagent {} not defined".format(
#                                 reagent))
#         return Model(states, reactions, output_frequency, output_reagents,
#                                             num_iterations, rng_seed, outFile)
