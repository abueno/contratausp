from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.forms import CustomAuthenticationForm

urlpatterns = patterns('accounts.views',
    url(r'^login/$', 'custom_login', {'authentication_form': CustomAuthenticationForm, 'template_name': 'accounts/login.html'}, name='login'),
    url(r'^alunos/(?P<login>[\w\.\-]+)$', 'profile_student', name='profile_student'),
    url(r'^empresas/(?P<login>[\w\.\-]+)$', 'profile_company', name='profile_company'),
    
) + patterns('django.contrib.auth.views',
    # --- Renaming of Django urls ---
    url(r'^logout/$', 'logout', name='logout')
)
