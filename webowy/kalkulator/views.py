from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def kalkulator(request:HttpRequest) -> HttpResponse:
    operacja = request.GET.get('operacja')
    arg1 = request.GET.get('arg1')
    arg2 = request.GET.get('arg2')

    if operacja and arg1 and arg2:
        liczba1 = int(arg1)
        liczba2 = int(arg2)
        if operacja == 'add': wynik = liczba1 + liczba2
        elif operacja == 'sub': wynik = liczba1 - liczba2
        elif operacja == 'mul': wynik = liczba1 * liczba2
        elif operacja == 'div': wynik = liczba1 / liczba2
        else: wynik = 0
    else:
        wynik = 0

    return render(request=request, template_name='kalkulator.html',
                  context={'wynik': wynik})
