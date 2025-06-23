from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    tipo = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self):
        return self.tipo

class Articulos(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=500)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    imagen = models.ImageField(upload_to='articulos/')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'articulo'
        verbose_name_plural = 'articulos'
    def __str__(self):
        return self.titulo
    