from django.urls import path
from . import views

urlpatterns = [
    path('', views.articulos, name="Articulos"),
    path('categoria/<int:categoria_id>', views.categoria, name= "Categoria")
]