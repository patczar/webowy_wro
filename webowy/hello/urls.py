from django.urls import path

import hello.views

urlpatterns = [
    path('', hello.views.wypisz_hello),
    path('hello.html', hello.views.wypisz_hello_html),
    path('szablon', hello.views.wypisz_hello_szablon),
    path('ping', hello.views.ping),
    path('rozmowa', hello.views.rozmowa),
    path('rozmowa.html', hello.views.rozmowa_html),
    path('rozmowa2.html', hello.views.rozmowa_szablon),
]
