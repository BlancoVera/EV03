from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProyectoWeb.urls')),
    path('articulos/', include('articulos.urls')),
    path('contacto/', include('contacto.urls')),
    path('tienda/', include('tienda.urls')),
    path('carrito/', include('carrito.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('pedidos/', include ('pedidos.urls'))
]
