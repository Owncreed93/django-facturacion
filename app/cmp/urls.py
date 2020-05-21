from django.urls import path

from .views import (
    ProveedorView,
    ProveedorNew,
    ProveedorEdit,
    proveedorInactivar,
)

urlpatterns = [
    # * PROVEEDORES
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedores/inactivar/<int:id>', proveedorInactivar, name="proveedor_inactivar"),
]
