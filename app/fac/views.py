from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from bases.views import SinPrivilegios


from .models import Cliente
from .forms import ClienteForm

# Create your views here.
class ClienteView(SinPrivilegios, generic.ListView):
    permission_required = 'cmp.view_cliente'
    model = Cliente
    template_name = 'cmp/cliente_list.html'
    context_object_name = 'obj'


class VistaBaseCreate(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    context_object_name = 'obj'
    success_message = 'Cliente agregado satisfactoriamente'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    context_object_name = 'obj'
    success_message = 'Cliente actualizado satisfactoriamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

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