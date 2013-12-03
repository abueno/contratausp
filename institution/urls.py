from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('institution.views',
    url(r'^$', 'all_institutions', name='all_institutions'),
    url(r'^(?P<institution_id>[0-9]+)$', 'institution', name='institution'),
)
