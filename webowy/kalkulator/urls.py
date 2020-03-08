from django.urls import path

import kalkulator.views

urlpatterns = [
    path('v1', kalkulator.views.kalkulator),

]
