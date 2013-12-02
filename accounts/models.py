# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink

class Tipo_permissao(models.Model):
    nome = models.CharField(max_length=100, verbose_name=u'Nome')

    def __unicode__(self):
        return self.name

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
        return ('accounts.views.profile', (self.username,))
    
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
        
class Aluno(BaseUser):
    id_aluno = models.OneToOneField(BaseUser, parent_link=True, related_name='aluno', primary_key=True)
    cpf = models.CharField(blank=False, null=False, verbose_name="CPF", max_length=12)
    ja_estagiou = models.BooleanField(default=False, verbose_name=u"Já Estagiou", help_text=u'Informa se o usuario já estagiou')
    data_nascimento = models.DateField(blank=False, null=False, verbose_name="Data de Nascimento")
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Alunos"
        
class Empregador(BaseUser):
    id_empregador = models.OneToOneField(BaseUser, parent_link=True, related_name='empregador', primary_key=True)
    ja_foi_aceito_pelo_secretario = models.BooleanField(default=False, verbose_name=u"Já foi aceito pelo secretário", help_text=u'Informa se o empregador já foi aceito pelo secretário')
    num_referencias_positivas = models.IntegerField(default=0, verbose_name=u"Número de referências positivas")
    num_referencias_negativas = models.IntegerField(default=0, verbose_name=u"Número de referências negativas")

    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Empregadores"