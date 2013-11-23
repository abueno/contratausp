from django.template.context import RequestContext
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html', {}, RequestContext(request))