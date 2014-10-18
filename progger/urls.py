from django.conf.urls import patterns, include, url
#from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'progger.views.home', name='home'),
    url(r'^$', 'progger.views.home', name='home'),
    url(r'^resume', 'progger.views.resume', name='resume'),
    
)
