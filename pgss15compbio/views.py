from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from skeletonpages.forms import AlgorithmRunForm
from django.core.urlresolvers import reverse
from skeletonpages.models import *

def hello(request):
  context = {'active_tab': '#index'}
  return render_to_response('common/welcome.html', context, RequestContext(request))