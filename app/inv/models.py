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
        return f'{self.description}'

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    

