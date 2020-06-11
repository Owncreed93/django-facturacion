from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)


from bases.views import (
    SinPrivilegios,
    VistaBaseCreate,
    VistaBaseEdit,
)
from .models import Cliente
from .forms import ClienteForm


# Create your views here.
class ClienteView(SinPrivilegios, ListView):
    permission_required = 'cmp.view_cliente'
    model = Cliente
    template_name = 'cmp/cliente_list.html'
    context_object_name = 'obj'


class ClienteNew(VistaBaseCreate):
    model=Cliente
    template_name = 'fac/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('fac:cliente_list')
    permission_required = 'fac.add_cliente'


class ClienteEdit(VistaBaseEdit):
    model= Cliente
    template_name = 'fac/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('fac:cliente_list')
    permission_required = 'fac.change_cliente'

@login_required(login_url="/login/")
@permission_required("fac.change_cliente", login_url='/login/')
def clienteInactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method == 'POST':
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse('OK')
    return HttpResponse('FAIL')   
    
    return HttpResponse('FAIL')