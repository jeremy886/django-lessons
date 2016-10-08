__author__ = 'Jeremy Chen'

from django.template import loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import render

def custom_proc(request):
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }

def view_1(request):
    return render(request, 'template1.html',
                  {'message': 'I am view ONE'},
                  context_instance=RequestContext(request, processors=[custom_proc])
                  )

def view_2(request):
    t = loader.get_template('template1.html')
    c = RequestContext(request, {'message': 'I am in view Two'}, processors=[custom_proc])
    return HttpResponse(t.render(c))