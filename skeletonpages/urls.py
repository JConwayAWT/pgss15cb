from django.conf.urls import url, include
from skeletonpages import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^input/$', views.input, name='input'),
  url(r'^output/$', views.output, name='output'),
  url(r'^about_us/$', views.about_us, name='about_us'),
  url(r'^instructions/$', views.instructions, name='instructions'),
  url(r'^file_test/$', views.file_test, name='file_test'),
  url(r'^simulations/(?P<simulation_id>\d+)/show', views.show_simulation, name="show_simulation"),
  url(r'^simulations/new/$', views.new_simulation, name="new_simulation"),
  url(r'^simulations/create/$', views.create_simulation, name="create_simulation"),
  url(r'^simulations/create/ajax$', views.create_simulation_ajax, name="create_simulation_ajax"),
  url(r'^simulations/(?P<simulation_id>\d+)/delete/$', views.del_simulation, name="del_simulation"),
  url(r'^keep_alive/$', views.keep_alive, name="keep_alive"),
  url(r'^simulation_running/$', views.simulation_running, name="simulation_running"),

]