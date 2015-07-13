from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
  context = {'active_tab': '#index'}
  return render_to_response('skeletonpages/index.html', context, RequestContext(request))

def input(request):
	context = {'active_tab': '#input-nav'}
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