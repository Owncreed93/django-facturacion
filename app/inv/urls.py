from django.urls import path

from .views import (
    # * CATEGORIA VIEWS
    CategoriaView,
    CategoriaNew,
    CategoriaEdit,
    CategoriaDel,
    # * SUBCATEGORIA VIEWS
    SubCategoriaView,
    SubCategoriaNew,
    SubCategoriaEdit,
    SubCategoriaDel,
    # * MARCA VIEWS
    MarcaView,
    MarcaNew,
    MarcaEdit,
    marca_inactivar,
    # * UNIDADES DE MEDIDA
    UMView,
    UMNew,
    UMEdit,
    um_inactivar,
    # * PRODUCTO
    ProductoView,
    ProductNew,
    ProductoEdit,
    producto_inactivar,
)

urlpatterns = [
    # * CATEGORIAS URL
    path('categorias/', CategoriaView.as_view(), name="categoria_list"),
    path('categorias/new', CategoriaNew.as_view(), name="categoria_new"),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name="categoria_edit"),
    path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name="categoria_del"),
    # * SUBCATEGORIAS URL
    path('subcategorias/', SubCategoriaView.as_view(), name="subcategoria_list"),
    path('subcategorias/new', SubCategoriaNew.as_view(), name="subcategoria_new"),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name="subcategoria_edit"),
    path('subcategorias/delete/<int:pk>', SubCategoriaDel.as_view(), name="subcategoria_del"),
    # * MARCAS URL
    path('marcas/', MarcaView.as_view(), name="marca_list"),
    path('marcas/new', MarcaNew.as_view(), name="marca_new"),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name="marca_edit"),
    path('marcas/inactivar/<int:id>', marca_inactivar, name="marca_inactivar"),
    # * UNIDADES MEDIDA URL
    path('unidadesmedida/', UMView.as_view(), name="um_list"),
    path('unidadesmedida/new', UMNew.as_view(), name="um_new"),
    path('unidadesmedida/edit/<int:pk>', UMEdit.as_view(), name="um_edit"),
    path('unidadesmedida/inactivar/<int:id>', um_inactivar, name="um_inactivar"),
    # * PRODUCTO
    path('productos/', ProductoView.as_view(), name="producto_list"),
    path('productos/new', ProductNew.as_view(), name="producto_new"),
    path('productos/edit/<int:pk>', ProductoEdit.as_view(), name="producto_edit"),
    path('producto/inactivar/<int:id>', producto_inactivar, name="producto_inactivar"),
]