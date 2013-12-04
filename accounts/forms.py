# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from accounts.models import Aluno, Fisico, Juridico, Aluno_curso, Endereco

class CustomAuthenticationForm(AuthenticationForm):
    # Increased max_length of username to acommodate e-mail addresses
    username = forms.CharField(label="Username", max_length=75)
    
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'e_mail', 'login', 'senha', 'cpf', 'data_nascimento']
        widgets = {
            'senha': forms.PasswordInput(),
        }
        
class AlunoEditForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'e_mail', 'login', 'cpf', 'data_nascimento']
        
class EmpregadorFisicoForm(forms.ModelForm):
    class Meta:
        model = Fisico
        fields = ['nome', 'e_mail', 'login', 'senha', 'cpf']
        widgets = {
            'senha': forms.PasswordInput(),
        }
        
class EmpregadorFisicoEditForm(forms.ModelForm):
    class Meta:
        model = Fisico
        fields = ['nome', 'e_mail', 'login', 'cpf']
        
class EmpregadorJuridicoForm(forms.ModelForm):
    class Meta:
        model = Juridico
        fields = ['nome', 'e_mail', 'login', 'senha', 'cnpj', 'numero_funcionarios']
        widgets = {
            'senha': forms.PasswordInput(),
        }
        
class EmpregadorJuridicoEditForm(forms.ModelForm):
    class Meta:
        model = Juridico
        fields = ['nome', 'e_mail', 'login', 'cnpj', 'numero_funcionarios']
        
class CursoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno_curso
        widgets = {
            'aluno': forms.HiddenInput()
        }
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Endereco
        widgets = {
            'empregador': forms.HiddenInput()
        }