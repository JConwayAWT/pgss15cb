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
  context = {'simulation': simulation}
  return render_to_response('skeletonpages/show_simulation.html', context, RequestContext(request))

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