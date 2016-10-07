__author__ = 'Jeremy Chen'

from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render
from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def hello(request):
    return HttpResponse('Hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    html = 'It is now %s.' % now
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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'], cd['message'], cd.get('email', 'noreply@example.com'), ['supamrchen@gmail.com'])
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})

def contact2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'], cd['message'], cd.get('email', 'noreply@example.com'), ['supamrchen@gmail.com'])
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form2.html', {'form': form})

def thankyou(request):
    return HttpResponse('Thank you!')