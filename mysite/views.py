__author__ = 'Jeremy Chen'

from django.http import HttpResponse, Http404
from django.template import Template, Context
import datetime

def hello(request):
    return HttpResponse('Hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    t = Template('<html><body>It is now {{current_date }}.</body></html>')
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    assert False
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = 'In %s hours(s), it will be %s.' % (offset, dt)

    return HttpResponse(html)