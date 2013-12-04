# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from institution.models import Faculdade, Curso_faculdade
from django.core.urlresolvers import reverse

class Tipo_permissao(models.Model):
    nome = models.CharField(max_length=100, verbose_name=u'Nome')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u"Tipo de permissão"
        verbose_name_plural = u"Tipos de Permissão"
        
class BaseUser(User):
    nome = models.CharField(blank=False, null=False, verbose_name=u'Nome', max_length=200)
    e_mail = models.CharField(blank=False, null=False, verbose_name=u'E-mail', max_length=200)
    login = models.CharField(blank=False, null=False, verbose_name=u'Login', max_length=100)
    senha = models.CharField(blank=False, null=False, verbose_name=u'Senha', max_length=128)
    tipo_permissao = models.ForeignKey(Tipo_permissao, related_name='tipo_permissao')
    is_admin = models.BooleanField(default=False, help_text=u'Informa se o usuario é um administrador do sistema.')
    
    def __unicode__(self):
        return self.username

    @permalink
    def get_absolute_url(self):
        if self.get_type() == 'aluno':
            return ('accounts:profile_student', (self.login,))
        elif self.get_type() == 'empregador':
            return ('accounts:profile_company', (self.login,))
    
    def get_type(self):
        try:
            if self.aluno:
                return "aluno"
        except:
            try:
                if self.empregador:
                    return "empregador"
            except:
                return "nenhum"
        
    def get_type_object(self):
        if self.get_type() == 'aluno':
            return self.aluno
        if self.get_type() == 'empregador':
            return self.empregador

    class Meta:
        verbose_name_plural = "Usuarios"
        ordering = ['username']

class Secretario(BaseUser):
    id_secretario = models.OneToOneField(BaseUser, parent_link=True, related_name='secretario', primary_key=True)
    faculdade = models.ForeignKey(Faculdade, related_name='secretario_percente_a_faculdade')
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = u"Secretários"
        
class Aluno(BaseUser):
    id_aluno = models.OneToOneField(BaseUser, parent_link=True, related_name='aluno', primary_key=True)
    cpf = models.CharField(blank=False, null=False, verbose_name="CPF", max_length=12)
    ja_estagiou = models.BooleanField(default=False, verbose_name=u"Já Estagiou", help_text=u'Informa se o usuario já estagiou')
    data_nascimento = models.DateField(blank=False, null=False, verbose_name="Data de Nascimento")
    
    def ja_quis_empresa(self, empregador):
        if Aluno_quer_empresa.objects.filter(aluno=self, empregador=empregador).exists():
            return True
        return False
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Alunos"
        
class Aluno_curso(models.Model):
    aluno = models.ForeignKey(Aluno, related_name='aluno_tem_curso')
    curso = models.ForeignKey(Curso_faculdade, related_name='aluno_tem_curso')
    situacao = models.CharField(max_length=100, verbose_name=u'Situação')
    ano_ingresso = models.IntegerField()

    def __unicode__(self):
        return self.aluno.nome + ' cursou ' + self.curso.nome

    class Meta:
        verbose_name = u"Aluno tem curso"
        verbose_name_plural = u"Aluno tem cursos"
        
class Empregador(BaseUser):
    id_empregador = models.OneToOneField(BaseUser, parent_link=True, related_name='empregador', primary_key=True)
    ja_foi_aceito_pelo_secretario = models.BooleanField(default=False, verbose_name=u"Já foi aceito pelo secretário", help_text=u'Informa se o empregador já foi aceito pelo secretário')
    num_referencias_positivas = models.IntegerField(default=0, verbose_name=u"Número de referências positivas")
    num_referencias_negativas = models.IntegerField(default=0, verbose_name=u"Número de referências negativas")

    @permalink
    def get_absolute_url(self):
        return ('accounts:profile_company', (self.login,))
        
    def get_type(self):
        try:
            if self.fisico:
                return 'fisico'
        except:
            if self.juridico:
                return 'juridico'
            
        return 'nenhum'
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Empregadores"
        
class Aluno_quer_empresa(models.Model):
    aluno = models.ForeignKey(Aluno, related_name='aluno_quer_empresa')
    empregador = models.ForeignKey(Empregador, related_name='aluno_quer_empresa')

    def __unicode__(self):
        return self.aluno.nome + ' quer trabalhar com ' + self.empregador.nome

    class Meta:
        verbose_name = u"Aluno quer empresa"
        verbose_name_plural = u"Alunos querem empresas"
        
class Fisico(Empregador):
    id_empregador_fisico = models.OneToOneField(Empregador, parent_link=True, related_name='fisico', primary_key=True)
    cpf = models.CharField(blank=False, null=False, verbose_name="CPF", max_length=12)
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Empregadores Físicos"
        
class Juridico(Empregador):
    id_empregador_juridico = models.OneToOneField(Empregador, parent_link=True, related_name='juridico', primary_key=True)
    cnpj = models.CharField(blank=False, null=False, verbose_name="CNPJ", max_length=14)
    numero_funcionarios = models.IntegerField(default=0, verbose_name=u"Número de funcionarios")

    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Empregadores Juridicos"
        
class Endereco(models.Model):
    logradouro = models.CharField(verbose_name=u'Logradouro', max_length=100)
    bairro = models.CharField(verbose_name=u'Bairro', max_length=100)
    cidade = models.CharField(verbose_name=u'Cidade', max_length=100)
    cep = models.CharField(verbose_name=u'CEP', max_length=9)
    empregador = models.ForeignKey(Empregador, related_name='empresa_tem_endereco')

    def __unicode__(self):
        return self.logradouro

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"