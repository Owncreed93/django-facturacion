from django import forms

from .models import (
    Proveedor,
    ComprasEnc
)

class ProveedorForm(forms.ModelForm):

    
    class Meta:
        model = Proveedor
        fields = [ 'descripcion', 'estado', 'direccion', 'contacto', 
            'telefono', 'email', ]
        exclude = [ 'um', 'fm', 'uc', 'fc' ]
        widget = { 'descripcion' : forms.TextInput }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
        self.fields['descripcion'].widget.attrs.update({'placeholder': 'Descripción'})
        self.fields['direccion'].widget.attrs.update({'placeholder': 'Dirección'})
        self.fields['contacto'].widget.attrs.update({'placeholder': 'Contacto'})
        self.fields['telefono'].widget.attrs.update({'placeholder': 'Telefono'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})


class ComprasEncForm(forms.ModelForm):
    fecha_compra = forms.DateInput()
    fecha_factura = forms.DateInput()

    class Meta:
        model = ComprasEnc
        fields = [
            'proveedor', 'fecha_compra', 'observacion',
            'no_factura', 'fecha_factura', 'sub_total',
            'descuento', 'total'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class' : 'form-control'
            })
        
        self.fields['fecha_compra'].widget.attrs['readonly'] = True
        self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True