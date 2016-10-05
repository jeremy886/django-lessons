from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book

def hello(request):
    return HttpResponse('Hello World!')

def current_url_view(request):
    return HttpResponse('Welcome to the page at %s' % request.path)

def display_ua(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknow')
    return HttpResponse('Your browser is %s' % ua)

def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search(request):
    error = False
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            error = True
        else:
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'search_results.html', {'books':books, 'query':query})
    return render(request, 'search_form.html', {'error':error})

def search2(request):
    errors = []
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            errors.append('Enter a search term.')
        elif len(query) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'search_results.html', {'books': books, 'query': query})
    return render(request, 'search_form2.html', {'errors': errors})