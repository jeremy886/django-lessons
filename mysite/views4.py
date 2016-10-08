__author__ = 'Jeremy Chen'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from mysite.forms import MessageForm

def hi(request):
    error = False
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            error = True
        else:
            return render(request, 'hiback.html', {'query': query})
    return render(request, 'sayhi.html', {'error':error})

def hello(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return render(request, 'helloback.html', {'message': cd['your_message']})
    else:
        form = MessageForm(initial={'your_message': 'Your site is fantastic!'})

    return render(request, 'sayhello.html', {'form': form})