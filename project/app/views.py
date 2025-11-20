from django.shortcuts import render
from django.http import JsonResponse
from .models import Cliente

# Create your views here.
def clientes(request):
    clientes = Cliente.objects.values()
    return JsonResponse(list(clientes), safe=False)