from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from mysite.forms import MessageForm
# Create your views here.

def write_review(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return render(request, 'show_review1.html', {'message': cd['your_message']})
    else:
        form = MessageForm(initial={'your_message': 'Your site is fantastic!'})

    return render(request, 'write_review.html', {'form': form})

def time_calc(request):
    return render(request, 'show_time.html')

def tz_time_calc(request):
    return render(request, 'show_time.html', {'timezone': 'Asia/Taipei'})