from django.db import models

from bases.models import ClaseModelo 


# Create your models here.
class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100, 
        help_text="Descripción de la categoría",
        unique=True
    )

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return f'{self.descripcion}'

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100, 
        help_text="Descripción de la subcategoría",
    )

    class Meta:
        verbose_name_plural = "Subcategorías"
        unique_together = ('categoria', 'descripcion')

    def __str__(self):
        return f'{self.categoria.descripcion} : {self.descripcion}'

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()
    

