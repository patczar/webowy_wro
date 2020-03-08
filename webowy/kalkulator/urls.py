from .views import *
from django.urls import path

urlpatterns = [
    path('', kalkulator2),
    path('v1', kalkulator1),
    path('v2', kalkulator2),
]
