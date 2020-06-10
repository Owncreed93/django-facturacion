from django.urls import path

from .views import (
    ClienteView,
    ClienteNew,
    ClienteEdit,
    clienteInactivar,
)

urlpatterns = [
    # * CLIENTES
    path('clientes/', ClienteView.as_view(), name='cliente_list'),
    path('clientes/new', ClienteNew.as_view(), name='cliente_new'),
    path('clientes/edit/<int:pk>', ClienteEdit.as_view(), name='cliente_edit'),
    path('clientes/estado/<int:id>', clienteInactivar, name='cliente_inactivar'),
]