from django.conf.urls import patterns, url
from photogallery import views


urlpatterns = patterns('',
                       
            url(r'^$', views.index, name='index'),
            )