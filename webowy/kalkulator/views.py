from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from kalkulator import logika


def kalkulator1(request: HttpRequest) -> HttpResponse:
    if 'arg1' in request.GET and 'arg2' in request.GET and 'operacja' in request.GET:
        operacja = request.GET['operacja']
        arg1 = int(request.GET['arg1'])
        arg2 = int(request.GET['arg2'])
        wynik = logika.oblicz(operacja, arg1, arg2)
    else:
        wynik = ''

    return render(request=request, template_name='kalkulator_get.html',
                  context={'wynik': wynik})


def kalkulator2(request: HttpRequest) -> HttpResponse:
    if 'arg1' in request.POST and 'arg2' in request.POST and 'operacja' in request.POST:
        # operacja = request.POST.get('operacja') # ta wersja zwraca None jeśli nie ma klucza
        operacja = request.POST['operacja'] # ta wersja wyrzuca wyjątek jeśli nie ma klucza
        arg1 = int(request.POST['arg1'])
        arg2 = int(request.POST['arg2'])
        wynik = logika.oblicz(operacja, arg1, arg2)
    else:
        wynik = ''

    return render(request=request, template_name='kalkulator_post.html',
                  context={'wynik': wynik})
