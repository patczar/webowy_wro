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


def ping(request: HttpRequest) -> HttpResponse:
    godzina:str = datetime.now().strftime('%H:%M:%S')
    ip = adres_klienta(request)
    przegladarka = request.headers.get('User-Agent')
    print(f'O godzinie {godzina} pingnął mnie {ip} z przeglądarki {przegladarka}')
    return HttpResponse(content=f'Hello, Twoje IP: {ip}, godzina {godzina}\nPrzeglądarka: {przegladarka}',
                        content_type='text/plain;charset=utf-8')

