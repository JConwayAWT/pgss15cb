from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
  context = RequestContext(request)
  #template = loader.get_template('skeletonpages/index.html')
  #return HttpResponse(template.render(context))
  return render_to_response('skeletonpages/index.html', RequestContext(request))

def input(request):
	context = RequestContext(request)
	return render_to_response('skeletonpages/input.html', RequestContext(request))

# Create your views here.
