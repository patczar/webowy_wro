from django.db import models

# Create your models here.

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    promocja = models.BooleanField()


class Zamowienie(models.Model):
    data = models.DateTimeField()
    adres_ulica = models.CharField(max_length=100)
    adres_miasto = models.CharField(max_length=50)
    adres_kod = models.CharField(max_length=10)


class TowarWZamowieniu(models.Model):
    zamowienie = models.ManyToManyField(Zamowienie)
    produkt = models.ManyToManyField(Produkt)
    ilosc = models.IntegerField()
