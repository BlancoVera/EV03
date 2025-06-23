from django.shortcuts import render, get_object_or_404
from .models import Articulos, Categoria

def articulos(request):
    articulos = Articulos.objects.all()
    categorias = Categoria.objects.all() 
    return render(request, "articulos/articulos.html", {
        'articulos': articulos, 
        'categorias': categorias, 
        })

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    articulos = Articulos.objects.filter(categorias=categoria)
    return render(request, "articulos/categorias.html", {
        'categoria': categoria, 
        'articulos': articulos
        })
