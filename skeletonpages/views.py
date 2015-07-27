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


def index(request):
  context = {'active_tab': '#index'}
  return render_to_response('skeletonpages/index.html', context, RequestContext(request))

def input(request):
  if request.method == 'POST':
    form = AlgorithmRunForm(request.POST, request.FILES)
    if form.is_valid():
      out_file = File(open("./pgss15compbio/media/out_file.csv", "w+"))
      p = Parser()
      model = p.get_model(request.FILES['input_file'], out_file)
      model.iterate()
      new_algorithm_run = AlgorithmRun(input_file=request.FILES['input_file'],
        output_file=out_file)
      new_algorithm_run.save()
      # Redirect to the document list after POST
      h = HttpResponseRedirect("../../media/out_file.csv")
      return h
  else:
    form = AlgorithmRunForm() # A empty, unbound form
  
  context = {'active_tab': '#input-nav', 'form': form}
  return render_to_response('skeletonpages/input.html', context, RequestContext(request))

def output(request):
  context = {'active_tab': '#output-nav'}
  return render_to_response('skeletonpages/output.html', context, RequestContext(request))

def instructions(request):
  context = {'active_tab': '#instructions-nav'}
  return render_to_response('skeletonpages/instructions.html', context, RequestContext(request))

def about_us(request):
  context = {'active_tab': '#about_us-nav'}
  return render_to_response('skeletonpages/about_us.html', context, RequestContext(request))

def show_simulation(request, simulation_id):
  simulation = AlgorithmRun.objects.get(pk = simulation_id)

  output_file = open(simulation.output_file.path, "r")
  first_line = output_file.readline()

  list_of_lists = []
  for variable_name in first_line.strip().split(","):
    list_of_lists.append([variable_name])

  for line in output_file.readlines():
    # ipdb.set_trace()
    split_line = line.split(",")
    for index, value in enumerate(split_line):
      list_of_lists[index].append(float(value.rstrip()))

  dictionary = {}
  for sublist in list_of_lists:
    dictionary.update( { sublist[0]: sublist[1:] } )

  values_dictionary_as_json = json.dumps(dictionary)

  # import ipdb
  # ipdb.set_trace()

  context = {'simulation': simulation, 'values': values_dictionary_as_json}



  return render_to_response('skeletonpages/show_simulation.html', context, RequestContext(request))

def new_simulation(request):
  form = AlgorithmRunForm()
  return render_to_response('skeletonpages/new_simulation.html', 
                            {'form': form}, 
                            context_instance = RequestContext(request))

def create_simulation(request):
  form = AlgorithmRunForm(request.POST, request.FILES)
  if form.is_valid():
    file_name = "./pgss15compbio/media/out_file_{}.txt".format( str(random())[2:] )
    out_file = File(open(file_name, "w+"))
    p = Parser()
    model = p.get_model(request.FILES['input_file'], out_file)
    model.iterate()
    new_algorithm_run = AlgorithmRun(input_file = request.FILES['input_file'],
      output_file = out_file, name=request.POST['name'],
      description = request.POST['description'])

    # import pdb
    # pdb.set_trace()

    new_algorithm_run.save()
    request.user.userprofile.algorithm_runs.add(new_algorithm_run)
    request.user.userprofile.save()

    context = {'simulation': new_algorithm_run}


    return render_to_response('skeletonpages/show_simulation.html',
      context,
      RequestContext(request)
      )

def file_test(request):
    # Handle file upload
    if request.method == 'POST':
        form = AlgorithmRunForm(request.POST, request.FILES)
        if form.is_valid():
            out_file = File(open("./pgss15compbio/media/out_file.txt", "w+"))
            p = Parser()
            model = p.get_model(request.FILES['input_file'], out_file)
            model.iterate()
            new_algorithm_run = AlgorithmRun(input_file = request.FILES['input_file'],
              output_file=out_file)
            new_algorithm_run.save()
            # Redirect to the document list after POST
            h = HttpResponseRedirect("../../media/out_file.txt")

            return h
            
    else:
        form = AlgorithmRunForm() # A empty, unbound form

    # Load documents for the list page
    algorithm_runs = AlgorithmRun.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'skeletonpages/file_test.html',
        {'algorithm_runs': algorithm_runs, 'form': form},
        context_instance=RequestContext(request)
    )