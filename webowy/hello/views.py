from datetime import datetime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def adres_klienta(request: HttpRequest):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        return request.META.get('HTTP_X_FORWARDED_FOR')
    else:
        return request.META.get('REMOTE_ADDR')


def wypisz_hello(request):
    print('ping')
    return HttpResponse('Hello world')


# tutaj używam "type hints", aby edytor lepiej podpowiadał, co mogę zrobić z danym parametrem
def ping(request: HttpRequest) -> HttpResponse:
    godzina:str = datetime.now().strftime('%H:%M:%S')
    ip = adres_klienta(request)
    przegladarka = request.headers.get('User-Agent')
    print(f'O godzinie {godzina} pingnął mnie {ip} z przeglądarki {przegladarka}')
    return HttpResponse(content=f'Hello, Twoje IP: {ip}, godzina {godzina}\nPrzeglądarka: {przegladarka}',
                        content_type='text/plain;charset=utf-8')


def rozmowa(request: HttpRequest) -> HttpResponse:
    imie = request.GET.get('imie')
    # jeżeli klient nie podała parametru, to wynikiem jest None (gdybym napisał GET[klucz], to byłby wyjątek)
    if imie:
        tekst = f'Witaj {imie}!'
    else:
        tekst = 'Podaj swoje imię w parametrze imie'
    return HttpResponse(content=tekst, content_type='text/plain;charset=utf-8')


