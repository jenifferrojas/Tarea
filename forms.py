from django.forms import ModelForm
from app.models import Categoria, Cliente, Productos, Vendedor

class categoriaf (ModelForm):
    class Meta:
        model = Categoria
        fields = ['codigo','nombre']

class clientef (ModelForm):
    class Meta:
        model = Cliente
        fields = ['codigo','nombres', 'direccion']


class productof (ModelForm):
    class Meta:
        model = Productos
        fields = ['codigo','idcategoria', 'nombre', 'fechavencimiento', 'precio']

class vendedorf (ModelForm):
    class Meta:
        model = Vendedor
        fields = ['codigo','nombres']
