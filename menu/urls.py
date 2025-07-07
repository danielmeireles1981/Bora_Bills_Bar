from django.urls import path
from .views import home, cardapio, curiosidade

urlpatterns = [
    path('', home, name='home'),
    path('cardapio/', cardapio, name='cardapio'),
    path('curiosidades/', curiosidade, name='curiosidades'),
]