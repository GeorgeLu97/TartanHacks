from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<username>[a-zA-Z0-9]+)/$', views.index, name='index'),
]