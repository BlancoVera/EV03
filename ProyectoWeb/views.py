from django.shortcuts import render, HttpResponse
from carrito.carrito import Carrito
def home(request):
    carrito = Carrito(request)
    return render(request, "Proyecto01/home.html")
