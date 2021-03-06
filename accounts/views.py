# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.views import login
from django.template.context import RequestContext
from accounts.models import BaseUser, Tipo_permissao, Empregador,\
    Aluno_quer_empresa
from accounts.forms import AlunoForm, AlunoEditForm, EmpregadorFisicoForm,\
    EmpregadorJuridicoForm, EmpregadorFisicoEditForm, EmpregadorJuridicoEditForm,\
    CursoAlunoForm, AddressForm
from django.contrib.auth.decorators import login_required
from internship.models import Estagio
from django.db import connection, transaction

def custom_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('/', **kwargs)
    return login(request, **kwargs)

def registration(request):
    return render_to_response('accounts/registration.html', {}, RequestContext(request))

def registration_complete(request):
    return render_to_response('accounts/registration_complete.html', {}, RequestContext(request))

def registration_student(request):
    if request.user.is_authenticated():
        return redirect(request.user.get_absolute_url() )
    
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            tipo = Tipo_permissao.objects.get(nome="Aluno")
            aluno = form.save(commit=False)
            aluno.username = aluno.login
            aluno.email = aluno.e_mail
            aluno.tipo_permissao = tipo
            aluno.set_password(aluno.senha)
            aluno.senha = aluno.password
            #aluno.is_active = False
            aluno.save()
            
            return redirect('accounts:registration_complete')
    else:
        form = AlunoForm()
    
    return render_to_response('accounts/registration_student.html', {'form': form}, RequestContext(request))

def registration_company_fisico(request):
    if request.user.is_authenticated():
        return redirect(request.user.get_absolute_url() )
    
    if request.method == 'POST':
        form = EmpregadorFisicoForm(request.POST)
        if form.is_valid():
            tipo = Tipo_permissao.objects.get(nome="Empregador")
            empregador = form.save(commit=False)
            empregador.username = empregador.login
            empregador.email = empregador.e_mail
            empregador.tipo_permissao = tipo
            empregador.set_password(empregador.senha)
            empregador.senha = empregador.password
            #empregador.is_active = False
            empregador.save()
            
            return redirect('accounts:registration_complete')
    else:
        form = EmpregadorFisicoForm()
    
    return render_to_response('accounts/registration_company_fisico.html', {'form': form}, RequestContext(request))

def registration_company_juridico(request):
    if request.user.is_authenticated():
        return redirect(request.user.get_absolute_url() )
    
    if request.method == 'POST':
        form = EmpregadorJuridicoForm(request.POST)
        if form.is_valid():
            tipo = Tipo_permissao.objects.get(nome="Aluno")
            empregador = form.save(commit=False)
            empregador.username = empregador.login
            empregador.email = empregador.e_mail
            empregador.tipo_permissao = tipo
            empregador.set_password(empregador.senha)
            empregador.senha = empregador.password
            #empregador.is_active = False
            empregador.save()
            
            return redirect('accounts:registration_complete')
    else:
        form = EmpregadorJuridicoForm()
    
    return render_to_response('accounts/registration_company_juridico.html', {'form': form}, RequestContext(request))

def all_companies(request):
    empregadores = Empregador.objects.raw('SELECT * FROM accounts_empregador')
    return render_to_response('accounts/all_companies.html', {'empregadores': empregadores}, RequestContext(request))

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
    
    aluno_pode_querer = False
    if request.user.is_authenticated() and not request.user == user and request.user.get_type() == 'aluno':
        if not request.user.aluno.ja_quis_empresa(user.empregador):
            aluno_pode_querer = True
            
    estagios = Estagio.objects.filter(endereco_empresa__empregador=user.empregador)
    
    return render_to_response('accounts/profile_company.html', {'user': user, 'aluno_pode_querer': aluno_pode_querer, 'estagios': estagios}, RequestContext(request))

@login_required
def profile_edit_student(request):
    if request.method == 'POST':
        form = AlunoEditForm(request.POST, instance=request.user.aluno)
        if form.is_valid():
            aluno = form.save()
            return redirect(request.user.get_absolute_url() )
    else:
        form = AlunoEditForm(instance=request.user.aluno)
    
    return render_to_response('accounts/profile_edit_student.html', {'form': form}, RequestContext(request))

@login_required
def profile_edit_company_fisico(request):
    if request.method == 'POST':
        form = EmpregadorFisicoEditForm(request.POST, instance=request.user.empregador.fisico)
        if form.is_valid():
            fisico = form.save()
            return redirect(request.user.get_absolute_url() )
    else:
        form = EmpregadorFisicoEditForm(instance=request.user.empregador.fisico)
    
    return render_to_response('accounts/profile_edit_company_fisico.html', {'form': form}, RequestContext(request))

@login_required
def profile_edit_company_juridico(request):
    if request.method == 'POST':
        form = EmpregadorJuridicoEditForm(request.POST, instance=request.user.empregador.juridico)
        if form.is_valid():
            juridico = form.save()
            return redirect(request.user.get_absolute_url() )
    else:
        form = EmpregadorJuridicoEditForm(instance=request.user.empregador.juridico)
    
    return render_to_response('accounts/profile_edit_company_juridico.html', {'form': form}, RequestContext(request))

@login_required
def add_course_student(request):
    if request.method == 'POST':
        form = CursoAlunoForm(request.POST)
        if form.is_valid():
            aluno_curso = form.save()
            return redirect(request.user.get_absolute_url() )
    else:
        form = CursoAlunoForm(initial={'aluno': request.user.aluno})
    
    return render_to_response('accounts/add_course_student.html', {'form': form}, RequestContext(request))

@login_required
def wish_company(request, login):
    try:
        user = BaseUser.objects.get(login=login)
    except:
        return redirect('home')
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO accounts_aluno_quer_empresa (aluno_id, empregador_id) VALUES (%s, %s)", [request.user.aluno.id, user.empregador.id])
    transaction.commit_unless_managed()
    
    return redirect(user.get_absolute_url() )

@login_required
def wished_companies(request):
    if not request.user.is_authenticated() or not request.user.get_type() == 'aluno':
        return redirect('home')
    
    interesses = Aluno_quer_empresa.objects.raw('SELECT * from accounts_aluno_quer_empresa where aluno_id = %s', [request.user.aluno.id])
    
    return render_to_response('accounts/wished_companies.html', {'interesses': interesses}, RequestContext(request))

@login_required
def add_address_company(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            endereco = form.save()
            return redirect(request.user.get_absolute_url() )
    else:
        form = AddressForm(initial={'empregador': request.user.empregador})
    
    return render_to_response('accounts/add_address_company.html', {'form': form}, RequestContext(request))