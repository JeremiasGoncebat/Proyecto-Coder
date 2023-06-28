from django import forms

class clienteFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    telefono=forms.IntegerField()

class vendedorFormulario(forms.Form):
    razon_social=forms.CharField(max_length=30)
    cuit=forms.IntegerField()
    telefono = forms.IntegerField()

class articulosFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    precio=forms.FloatField()
    rubro= forms.CharField(max_length=30)