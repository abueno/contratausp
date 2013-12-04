from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'contratausp.views.home', name='home'),
    url(r'^usuarios/', include('accounts.urls', 'accounts')),
    url(r'^faculdades/', include('institution.urls', 'institution')),
    url(r'^estagios/', include('internship.urls', 'internship')),
    
    # url(r'^contratausp/', include('contratausp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
