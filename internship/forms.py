# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from accounts.models import Aluno, Fisico, Juridico, Aluno_curso, Endereco
from internship.models import Estagio

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Estagio
        exclude = ['aluno']
