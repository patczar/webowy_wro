from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Produkt

# Create your views here.
def lista_towarow(request:HttpRequest) -> HttpResponse:
    produkty = Produkt.objects.all()

    return render(request=request,
                  template_name='towary.html',
                  context={'towary': produkty})
