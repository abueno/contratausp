# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('internship.views',
    url(r'^adicionar-estagio/$', 'add_internship', name='add_internship'),
    
    url(r'^(?P<internship_id>[\w\.\-]+)$', 'internship', name='internship'),
)
