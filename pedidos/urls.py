from django.urls import path
from . import views

urlpatterns = [
    path('', views.procesar_pedido, name="Procesar_pedido"),
]

