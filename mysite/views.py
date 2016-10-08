__author__ = 'Jeremy Chen'
from django.template import loader, Context
from django.http import HttpResponse

def view_1(request):
    t = loader.get_template('template1.html')
    c = Context({''
                 'app': 'My app',
                 'user': request.user,
                 'ip_address': request.META['REMOTE_ADDR'],
                 'message': 'I am view number 1'
                 })
    return HttpResponse(t.render(c))

def view_2(request):
    t = loader.get_template('template2.html')
    c = Context({''
                 'app': 'My app',
                 'user': request.user,
                 'ip_address': request.META['REMOTE_ADDR'],
                 'message': 'I am view number 2'
                 })
    return HttpResponse(t.render(c))

