from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.order_by('-pontos', 'nome')
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

from django.shortcuts import render
from .models import Cliente

def leaderboard(request):
    clientes = Cliente.objects.order_by('-pontos', 'nome')
    return render(request, 'clientes/leaderboard.html', {'clientes': clientes})

from django.shortcuts import render
from .models import Cliente
from .utils import buscar_personagem_dbz

def leaderboard(request):
    clientes = Cliente.objects.order_by('-pontos', 'nome')
    # Enriquecer clientes com info do personagem favorito:
    clientes_enriquecidos = []
    for cliente in clientes:
        personagem_info = None
        if cliente.personagem_favorito:
            personagem_info = buscar_personagem_dbz(cliente.personagem_favorito)
        clientes_enriquecidos.append((cliente, personagem_info))
    return render(request, 'clientes/leaderboard.html', {'clientes_info': clientes_enriquecidos})
