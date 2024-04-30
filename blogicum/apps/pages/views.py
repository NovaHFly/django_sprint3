from django.shortcuts import HttpResponse, render

# Create your views here.


def about(request):
    return HttpResponse('<h1>About</h1>')


def rules(request):
    return HttpResponse('<h1>Rules</h1>')
