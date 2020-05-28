from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
import json

from .models import Proveedor
from .forms import ProveedorForm

from bases.views import SinPrivilegios

# Create your views here.
class ProveedorView(SinPrivilegios, generic.ListView):
    permission_required = 'cmp.view_proveedor'
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'

class ProveedorNew(SinPrivilegios, generic.CreateView):
    permission_required = 'cmp.add_proveedor'
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user

        return super().form_valid(form)


class ProveedorEdit(SinPrivilegios, generic.UpdateView):
    permission_required = 'cmp.change_proveedor'
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id

        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('cmp:change_proveedor', login_url='bases_sin_privilegio')
def proveedorInactivar(request, id):
    # * GET THE MARCA OBJECT
    proveedor = Proveedor.objects.filter(pk = id).first()

    # * CONTEXTO --> WHERE THE OBJECT WILL BE STORED
    contexto = {}

    # * TEMPLATE PATH
    template_name = 'cmp/inactivar_prv.html'

    if not proveedor:
        return HttpResponse(f'Proveedor no existe {id}.')

    if request.method == 'GET':
        contexto = { 'obj' : proveedor }

    if request.method == 'POST':
        proveedor.estado = False
        proveedor.save()
        contexto = {'obj' : 'OK'}

        return HttpResponse(f'Proveedor \'{proveedor.descripcion}\' inactivado.')

    return render(request, template_name, contexto)