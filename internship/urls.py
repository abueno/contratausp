# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('internship.views',
    url(r'^$', 'all_internships', name='all_internships'),
    url(r'^adicionar-estagio/$', 'add_internship', name='add_internship'),
    url(r'^desejar/(?P<internship_id>[\w\.\-]+)$', 'wish_internship', name='wish_internship'),
    url(r'^interesse/$', 'wished_internships', name='wished_internships'),
    url(r'^(?P<internship_id>[\w\.\-]+)$', 'internship', name='internship'),
)
