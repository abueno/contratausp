from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext

def home(request):
    return render_to_response('home.html', {}, RequestContext(request))