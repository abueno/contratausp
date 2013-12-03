# -*- coding: utf-8 -*-
from institution.models import Faculdade
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

def all_institutions(request):
    institutions = Faculdade.objects.all()
    
    return render_to_response('institution/all_institutions.html', {'institutions': institutions}, RequestContext(request))

def institution(request, institution_id):
    try:
        institution = Faculdade.objects.get(pk=institution_id)
    except:
        return redirect('home')
    
    return render_to_response('institution/institution.html', {'institution': institution}, RequestContext(request))