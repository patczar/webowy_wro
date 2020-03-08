from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def wypisz_hello(request):
    return HttpResponse(content='Hello world')
