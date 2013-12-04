# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from internship.forms import InternshipForm
from internship.models import Estagio, Aluno_quer_estagio
from django.db import connection, transaction

def all_internships(request):
    estagios = Estagio.objects.raw('SELECT e.*, end.empregador_id FROM internship_estagio e LEFT OUTER JOIN accounts_endereco end ON e.endereco_empresa_id = end.id')
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
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO internship_aluno_quer_estagio (aluno_id, estagio_id) VALUES (%s, %s)", [request.user.aluno.id, estagio.id])
    transaction.commit_unless_managed()
    
    return redirect(estagio.get_absolute_url() )

@login_required
def wished_internships(request):
    if not request.user.is_authenticated() or not request.user.get_type() == 'aluno':
        return redirect('home')
    
    interesses = Aluno_quer_estagio.objects.raw('SELECT * from internship_aluno_quer_estagio where aluno_id = %s', [request.user.aluno.id])
    
    return render_to_response('internship/wished_internships.html', {'interesses': interesses}, RequestContext(request))

def internship(request, internship_id):
    try:
        estagio = Estagio.objects.get(id=internship_id)
    except:
        return redirect('home')
    
    aluno_pode_desejar = False
    if request.user.is_authenticated() and request.user.get_type() == 'aluno' and not Aluno_quer_estagio.objects.filter(aluno=request.user.aluno, estagio=estagio).exists():
        aluno_pode_desejar = True
        
    desejos = None
    if request.user == estagio.endereco_empresa.empregador.id_empregador:
        desejos = Aluno_quer_estagio.objects.filter(estagio=estagio)
    
    return render_to_response('internship/internship.html', {'estagio': estagio, 'aluno_pode_desejar': aluno_pode_desejar, 'desejos': desejos}, RequestContext(request))
