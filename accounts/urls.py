from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.forms import CustomAuthenticationForm

urlpatterns = patterns('accounts.views',
    url(r'^login/$', 'custom_login', {'authentication_form': CustomAuthenticationForm, 'template_name': 'accounts/login.html'}, name='login')
) + patterns('django.contrib.auth.views',
    # --- Renaming of Django urls ---
    url(r'^logout/$', 'logout', name='logout')
)
