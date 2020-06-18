from django.urls import path

from .views import (
    ClienteView,
    ClienteNew,
    ClienteEdit,
    clienteInactivar,
    FacturaView,
    facturas,
    ProductoView,
)

urlpatterns = [
    # * CLIENTES
    path('clientes/', ClienteView.as_view(), name='cliente_list'),
    path('clientes/new', ClienteNew.as_view(), name='cliente_new'),
    path('clientes/edit/<int:pk>', ClienteEdit.as_view(), name='cliente_edit'),
    path('clientes/estado/<int:id>', clienteInactivar, name='cliente_inactivar'),
    # * FACTURAS
    path('facturas/', FacturaView.as_view(), name="factura_list"),
    path('facturas/new', facturas, name="factura_new"),
    path('facturas/buscar-producto', ProductoView.as_view(), name='factura_producto'),
]
