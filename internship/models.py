# -*- coding: utf-8 -*-
from django.db import models
from accounts.models import Aluno, Endereco
from django.db.models import permalink

class Estagio(models.Model):
    carga_horaria = models.IntegerField(verbose_name=u'Carga Horária')
    objetivo = models.CharField(max_length=50, verbose_name=u'Objetivo')
    duracao = models.CharField(max_length=50, verbose_name=u'Duração')
    nome = models.CharField(max_length=50, verbose_name=u'Nome')
    salario = models.DecimalField(decimal_places=2, max_digits=8, verbose_name=u'Salário')
    data_cadastro = models.DateField(auto_now_add=True, verbose_name=u'Data de Cadastro')
    vale_transporte = models.CharField(max_length=20, verbose_name=u'Vale Transporte')
    vale_refeicao = models.CharField(max_length=20, verbose_name=u'Vale Refeição')
    outros = models.CharField(max_length=50, verbose_name=u'Outros')
    data_inicio = models.DateField(verbose_name=u'Data de Início')
    data_fim = models.DateField(verbose_name=u'Data de Fim')
    aluno = models.ForeignKey(Aluno, related_name='historico_estagio_aluno', null=True)
    endereco_empresa = models.ForeignKey(Endereco, related_name='estagio_tem_endereco_da_empresa')
    
    @permalink
    def get_absolute_url(self):
        return ('internship:internship', (self.id,))

class Aluno_quer_estagio(models.Model):
    aluno = models.ForeignKey(Aluno, related_name="aluno_quer_estagio")
    estagio = models.ForeignKey(Estagio, related_name="aluno_quer_estagio")