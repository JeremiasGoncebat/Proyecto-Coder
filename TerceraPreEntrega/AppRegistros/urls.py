from django.urls import path
from AppRegistros import views

urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('clientes/', views.clientes, name="Clientes"),
    path('vendedores/', views.vendedores, name="Vendedores"),
    path('articulos/', views.articulos, name="Articulos"),
    path('busquedaArticulos/', views.BusquedaArticulos, name="BusquedaArticulos"),
    path('busquedaArticulos/buscar/',views.buscar, name="Buscar")
]
