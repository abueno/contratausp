# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.views import login

def custom_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('/', **kwargs)
    return login(request, **kwargs)