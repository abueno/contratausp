# Create your views here.
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.views import login
from django.template.context import RequestContext
from accounts.models import BaseUser

def custom_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('/', **kwargs)
    return login(request, **kwargs)

def profile_student(request, login):
    try:
        user = BaseUser.objects.get(login=login)
        if not user.get_type() == 'aluno':
            return redirect('home')
    except:
        return redirect('home')
    return render_to_response('accounts/profile_student.html', {'user': user}, RequestContext(request))

def profile_company(request, login):
    try:
        user = BaseUser.objects.get(login=login)
        if not user.get_type() == 'empregador':
            return redirect('home')
    except:
        return redirect('home')
    return render_to_response('accounts/profile_company.html', {'user': user}, RequestContext(request))