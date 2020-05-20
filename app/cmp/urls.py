from django.urls import path

from .views import (
    ProveedorView,
    ProveedorNew,
    ProveedorEdit,
    proveedor_inactivar,
)

urlpatterns = [
    # * PROVEEDORES
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactivar/<int:id>', proveedor_inactivar, name='proveedor_inactivar'),
]
