from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from skeletonpages.forms import AlgorithmRunForm
from django.core.urlresolvers import reverse
from skeletonpages.models import *

def hello(request):
  context = {'active_tab': '#index'}
  if request.user.is_authenticated():
    username = request.user.username
    profile = request.user.userprofile
    context = {'profile': profile, 'user': request.user}
    return render_to_response('userena/profile_detail.html', context, RequestContext(request))
  else:
    return render_to_response('common/welcome.html', context, RequestContext(request))