from django.urls import path

from .views import (
    ClienteView,
    ClienteNew,
    ClienteEdit,
    clienteInactivar,
    FacturaView,
    facturas,
    ProductoView,
    borrar_detalle_factura,
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
    path('facturas/edit/<int:id>', facturas, name="factura_edit"),
    # * FACTURAS - BÚSQUEDA PRODUCTO
    path('facturas/buscar-producto', ProductoView.as_view(), name='factura_producto'),
    # * FACTURAS - BORRAR DETALLE
    path('facturas/borrar-detalle/<int:id>', borrar_detalle_factura, name='factura_borrar_detalle'),
]
