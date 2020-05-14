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
]