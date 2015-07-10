from django.conf.urls import url, include
from skeletonpages import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^input/$', views.input, name='input'),
  url(r'^output/$', views.output, name='output'),
]