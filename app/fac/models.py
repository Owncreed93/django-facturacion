from django.db import models


from bases.models import ClaseModelo, ClaseModeloDos
from inv.models import Producto
# Create your models here.


class Cliente(ClaseModelo):
    NAT = 'Narutal'
    JUR = 'Jurídica'
    TIPO_CLIENTE = [ 
        (NAT, 'Natural'),
        (JUR, 'Jurídica'),
    ]
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    celular = models.CharField(
        max_length=20,
        null = True,
        blank = True,
    )
    tipo = models.CharField(
        max_length=10,
        choices = TIPO_CLIENTE,
        default = NAT
    )

    def __str__(self):
        return f'{self.apellidos} {self.nombres}'
    
    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural = 'Clientes'

class FacturaEnc(ClaseModeloDos):
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return f'{self.id}'
    
    def save(self):
        self.total = float(self.sub_total) - float(self.descuento)
        super(FacturaEnc, self).save()
    
    class Meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name = "Encabezado Factura"


class FacturaDet(ClaseModeloDos):
    factura = models.ForeignKey(FacturaEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return f'{self.producto}'

    def save(self):
        self.sub_total = float( float( int(self.cantidad) ) * float(self.precio) )
        self.total = self.sub_total - float(self.descuento)
        super(FacturaDet, self).save()

    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name = "Detalle Factura"
    

    
