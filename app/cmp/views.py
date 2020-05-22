from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import json

from .models import Proveedor
from .forms import ProveedorForm

# Create your views here.
class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user

        return super().form_valid(form)


class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id

        return super().form_valid(form)

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