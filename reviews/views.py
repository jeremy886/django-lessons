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

def time_inc(request):
    time_str_local = '12:17 PM, Sunday, 2016 10 16'
    time_str_taipei = '09:17 AM, Sunday, 2016 10 16'
    return render(request, 'show_time2.html', {'time_local': time_str_local, 'time_taipei': time_str_taipei })