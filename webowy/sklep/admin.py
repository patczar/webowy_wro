from django.contrib import admin

# Z modułu models znajdującego się bieżącym pakiecie (sklep)
# importuję wszystkie klasy
from .models import *

# Register your models here.
admin.site.register(Produkt)
admin.site.register(Zamowienie)
admin.site.register(TowarWZamowieniu)
