from django.conf.urls import url, include
from skeletonpages import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^input/$', views.input, name='input'),
  url(r'^output/$', views.output, name='output'),
  url(r'^about_us/$', views.about_us, name='about_us'),
  url(r'^instructions/$', views.instructions, name='instructions'),
  
  
  
]