from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.forms import CustomAuthenticationForm

urlpatterns = patterns('accounts.views',
    url(r'^login/$', 'custom_login', {'authentication_form': CustomAuthenticationForm, 'template_name': 'accounts/login.html'}, name='login'),

    url(r'^empresas/$', 'all_companies', name='all_companies'),
        
    url(r'^alunos/(?P<login>[\w\.\-]+)$', 'profile_student', name='profile_student'),
    url(r'^empresas/(?P<login>[\w\.\-]+)$', 'profile_company', name='profile_company'),
    
    url(r'^cadastro/$', 'registration', name='registration'),
    url(r'^cadastro-completo/$', 'registration_complete', name='registration_complete'),
    url(r'^alunos/cadastro/$', 'registration_student', name='registration_student'),
    url(r'^empresas/cadastro/fisico/$', 'registration_company_fisico', name='registration_company_fisico'),
    url(r'^empresas/cadastro/juridico/$', 'registration_company_juridico', name='registration_company_juridico'),
    
    url(r'^alunos/editar/$', 'profile_edit_student', name='profile_edit_student'),
    url(r'^empresas/fisico/editar/$', 'profile_edit_company_fisico', name='profile_edit_company_fisico'),
    url(r'^empresas/juridico/editar/$', 'profile_edit_company_juridico', name='profile_edit_company_juridico'),
    
    url(r'^alunos/adicionar-curso/$', 'add_course_student', name='add_course_student'),
    
) + patterns('django.contrib.auth.views',
    # --- Renaming of Django urls ---
    url(r'^logout/$', 'logout', name='logout')
)
