from django.shortcuts import render
from django.views import generic


from bases.views import SinPrivilegios


from .models import Cliente


# Create your views here.
class ClienteView(SinPrivilegios, generic.ListView):
    permission_required = 'cmp.view_cliente'
    model = Cliente
    template_name = 'cmp/cliente_list.html'
    context_object_name = 'obj'