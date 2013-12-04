# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from internship.forms import InternshipForm
from internship.models import Estagio, Aluno_quer_estagio

def all_internships(request):
    estagios = Estagio.objects.all()
    return render_to_response('internship/all_internships.html', {'estagios': estagios}, RequestContext(request))

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
def wish_internship(request, internship_id):
    try:
        estagio = Estagio.objects.get(id=internship_id)
    except:
        return redirect('home')
    
    obj = Aluno_quer_estagio.objects.get_or_create(aluno=request.user.aluno, estagio=estagio)
    
    return redirect(estagio.get_absolute_url() )

def internship(request, internship_id):
    try:
        estagio = Estagio.objects.get(id=internship_id)
    except:
        return redirect('home')
    
    aluno_pode_desejar = False
    if request.user.is_authenticated() and request.user.get_type() == 'aluno' and not Aluno_quer_estagio.objects.filter(aluno=request.user.aluno, estagio=estagio).exists():
        aluno_pode_desejar = True
    
    return render_to_response('internship/internship.html', {'estagio': estagio, 'aluno_pode_desejar': aluno_pode_desejar}, RequestContext(request))
