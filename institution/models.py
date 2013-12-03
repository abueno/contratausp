# -*- coding: utf-8 -*-
from django.db import models

class Faculdade(models.Model):
    sigla = models.CharField(max_length=10, verbose_name=u'Sigla')
    nome = models.CharField(max_length=200, verbose_name=u'Nome')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u"Faculdade"
        verbose_name_plural = u"Faculdades"
        
class Curso_faculdade(models.Model):
    sigla = models.CharField(max_length=10, verbose_name=u'Sigla')
    nome = models.CharField(max_length=200, verbose_name=u'Nome')
    duracao = models.CharField(max_length=200, verbose_name=u'Duração')
    periodo = models.CharField(max_length=200, verbose_name=u'Período')
    faculdade = models.ForeignKey(Faculdade, related_name='faculdade_possui_cursos')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u"Curso"
        verbose_name_plural = u"Cursos"