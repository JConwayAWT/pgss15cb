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

def del_simulation(request, simulation_id):
  simulation = AlgorithmRun.objects.get(pk = simulation_id)
  simulation.delete()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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

  keys = []
  for sublist in list_of_lists:
    keys.append(sublist[0])

  context = {'simulation': simulation, 'simulation_values': mark_safe(dictionary), 'variable_names': keys}

  return render_to_response('skeletonpages/show_simulation.html', context, RequestContext(request))

def new_simulation(request):
  form = AlgorithmRunForm()
  return render_to_response('skeletonpages/new_simulation.html', 
                            {'form': form}, 
                            context_instance = RequestContext(request))

def create_simulation_ajax(request):
  if request.GET:
    try:
      in_file = File(open("./pgss15compbio/media/temp.txt", "w+"))
      in_file.write(request.GET['str'])
      Parser.Parser().get_model(in_file, 'hello')
      return HttpResponse("1")
    except ValueError:
      return HttpResponse(status=412)
  print request.POST
  form = AlgorithmRunForm(request.POST, request.FILES)
  if form.is_valid():
    file_name = "./pgss15compbio/media/out_file_{}.txt".format( str(random())[2:] )
    out_file = File(open(file_name, "w+"))
    p = Parser.Parser()
    model = p.get_model(request.FILES['input_file'], out_file)
    model.iterate()
    new_algorithm_run = AlgorithmRun(input_file = request.FILES['input_file'],
      output_file = out_file, name=request.POST['name'],
      description = request.POST['description'])

    new_algorithm_run.save()
    request.user.userprofile.algorithm_runs.add(new_algorithm_run)
    request.user.userprofile.save()

    output_file = open(new_algorithm_run.output_file.path, "r")
    first_line = output_file.readline()

    list_of_lists = []
    for variable_name in first_line.strip().split(","):
      list_of_lists.append([variable_name])

    for line in output_file.readlines():
      split_line = line.split(",")
      for index, value in enumerate(split_line):
        list_of_lists[index].append(float(value.rstrip()))

    dictionary = {}
    for sublist in list_of_lists:
      dictionary.update( { sublist[0]: sublist[1:] } )

    keys = []
    for sublist in list_of_lists:
      keys.append(sublist[0])

    context = {'simulation': new_algorithm_run, 'simulation_values': mark_safe(dictionary), 'variable_names': keys}

    return render_to_response('skeletonpages/show_simulation.html', context, RequestContext(request))

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

    new_algorithm_run.save()
    request.user.userprofile.algorithm_runs.add(new_algorithm_run)
    request.user.userprofile.save()

    output_file = open(new_algorithm_run.output_file.path, "r")
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
      
    keys = []
    for sublist in list_of_lists:
      keys.append(sublist[0])

    context = {'simulation': simulation, 'simulation_values': mark_safe(dictionary), 'variable_names': keys}


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