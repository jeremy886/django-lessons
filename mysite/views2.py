__author__ = 'Jeremy Chen'

from django.template import loader, RequestContext
from django.http import HttpResponse

def custom_proc(request):
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }

def view_1(request):
    t = loader.get_template('template1.html')
    c = RequestContext(request, {'message': 'I am in view no. 1'}, processors=[custom_proc])
    return HttpResponse(t.render(c))

def view_2(request):
    t = loader.get_template('template1.html')
    c = RequestContext(request, {'message': 'I am in view no. 2'}, processors=[custom_proc])
    return HttpResponse(t.render(c))