from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


from .models import (
    Categoria,
    SubCategoria,
    Marca,
    UnidadMedida,
    Producto,
)
from .forms import (
    CategoriaForm,
    SubCategoriaForm,
    MarcaForm,
    UMForm,
    ProductoForm,
)

from bases.views import (
    SinPrivilegios,
    VistaBaseCreate,
    VistaBaseEdit,
    VistaBaseDelete,
)

# Create your views here.
class CategoriaView(SinPrivilegios, ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = "obj"


class CategoriaNew(VistaBaseCreate):
    permission_required = "inv.add_categoria"
    model = Categoria
    template_name = 'inv/categoria_form.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')


class CategoriaEdit(VistaBaseEdit):
    permission_required = "inv.change_categoria"
    model = Categoria
    template_name = 'inv/categoria_form.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')


class CategoriaDel(VistaBaseDelete):
    permission_required = "inv.change_categoria"
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    success_url = reverse_lazy('inv:categoria_list')


class SubCategoriaView(SinPrivilegios, ListView):
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = "obj"


class SubCategoriaNew(VistaBaseCreate):
    permission_required = "inv.add_subcategoria"
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')


class SubCategoriaEdit(VistaBaseEdit):
    permission_required = "inv.change_subcategoria"
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')


class SubCategoriaDel(VistaBaseDelete):
    permission_required = "inv.delete_subcategoria"
    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    success_url = reverse_lazy('inv:subcategoria_list')


class MarcaView(SinPrivilegios, ListView):
    permission_required = "inv.view_marca"
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = "obj"


class MarcaNew(VistaBaseCreate):
    permission_required = "inv.add_marca"
    model = Marca
    template_name = 'inv/marca_form.html'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')


class MarcaEdit(VistaBaseEdit):
    permission_required = "inv.change_marca"
    model = Marca
    template_name = 'inv/marca_form.html'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')


@login_required(login_url='/login/')
@permission_required('inv:change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request, id):
    # * GET THE MARCA OBJECT
    marca = Marca.objects.filter(pk = id).first()

    # * CONTEXTO --> WHERE THE OBJECT WILL BE STORED
    contexto = {}

    # * TEMPLATE PATH
    template_name = 'inv/catalogos_del.html'

    if not marca:
        return redirect('inv:marca_list')

    if request.method == 'GET':
        contexto = { 'obj' : marca }

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.error(request, f'Marca \'{marca.descripcion}\' Inactivada.')
        return redirect('inv:marca_list')

    return render(request, template_name, contexto)


class UMView(SinPrivilegios, ListView):
    permission_required = 'inv.view_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/um_list.html'
    context_object_name = "obj"


class UMNew(VistaBaseCreate):
    permission_required = 'inv.add_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/um_form.html'
    form_class = UMForm
    success_url = reverse_lazy('inv:um_list')


class UMEdit(VistaBaseEdit):
    permission_required = 'inv.change_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/um_form.html'
    form_class = UMForm
    success_url = reverse_lazy('inv:um_list')


@login_required(login_url='/login/')
@permission_required('inv:change_unidadmedida', login_url='bases:sin_privilegios')
def um_inactivar(request, id):
    # * GET THE MARCA OBJECT
    um = UnidadMedida.objects.filter(pk = id).first()

    # * CONTEXTO --> WHERE THE OBJECT WILL BE STORED
    contexto = {}

    # * TEMPLATE PATH
    template_name = 'inv/catalogos_del.html'

    if not um:
        return redirect('inv:um_list')

    if request.method == 'GET':
        contexto = { 'obj' : um }

    if request.method == 'POST':
        um.estado = False
        um.save()
        messages.error(request, f'Unidad de Medida \'{um.descripcion}\' Inactivada.')

        return redirect('inv:um_list')

    return render(request, template_name, contexto)


# * PRODUCTS VIEWS
class ProductoView(SinPrivilegios, ListView):
    permission_required = 'inv.view_producto'
    model = Producto
    template_name = 'inv/producto_list.html'
    context_object_name = "obj"


class ProductNew(VistaBaseCreate):
    permission_required = 'inv.add_producto'
    model = Producto
    template_name = 'inv/producto_form.html'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')


class ProductoEdit(VistaBaseEdit):
    permission_required = 'inv.change_producto'
    model = Producto
    template_name = 'inv/producto_form.html'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')


@login_required(login_url='/login/')
@permission_required('inv:change_producto', login_url='bases:sin_privilegios')
def producto_inactivar(request, id):
    # * GET THE MARCA OBJECT
    producto = Producto.objects.filter(pk = id).first()

    # * CONTEXTO --> WHERE THE OBJECT WILL BE STORED
    contexto = {}

    # * TEMPLATE PATH
    template_name = 'inv/catalogos_del.html'

    if not producto:
        return redirect('inv:producto_list')

    if request.method == 'GET':
        contexto = { 'obj' : producto }

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        messages.error(request, f'Producto \'{producto.descripcion}\' Inactivado.')

        return redirect('inv:producto_list')

    return render(request, template_name, contexto)
