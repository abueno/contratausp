# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from internship.forms import InternshipForm
from internship.models import Estagio

@login_required
def add_internship(request):
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            estagio = form.save()
            return redirect(estagio.get_absolute_url() )
    else:
        form = InternshipForm(initial={'endereco': request.user.empregador.empresa_tem_endereco.all() })
    
    return render_to_response('internship/add_internship.html', {'form': form}, RequestContext(request))

@login_required
def internship(request, internship_id):
    try:
        estagio = Estagio.objects.get(id=internship_id)
    except:
        return redirect('home')
    
    return render_to_response('internship/internship.html', {'estagio': estagio}, RequestContext(request))