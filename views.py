from django.shortcuts import render, redirect
from app.models import Categoria, Cliente, Productos, Vendedor
from app.forms import categoriaf, clientef, productof, vendedorf 

def home(request):
    return render(request, 'home.html')

#categoria
def catego(request):
    cate = Categoria.objects.all()
    context = {'cate':cate}
    return render (request, 'categoria.html',context )

def ggcatego (request):
    if request.method == 'POST':
        formulario = categoriaf  (request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('catego')
    else:
        formulario = categoriaf ()
        return render (request, 'agg_cate.html', {'formulario':formulario})
    

#cliente
def clien(request):
    clie = Cliente.objects.all()
    context = {'clie':clie}
    return render (request, 'cliente.html',context )

def ggclien (request):
    if request.method == 'POST':
        formulario = clientef  (request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('clien')
    else:
        formulario = clientef ()
        return render (request, 'agg_clie.html', {'formulario':formulario})
    

#producto
def produ(request):
    prod = Productos.objects.all()
    context = {'prod':prod}
    return render (request, 'producto.html',context )

def ggprod (request):
   if request.method == 'POST':
        formulario = productof  (request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('produc')
   else:
        formulario = productof ()
        return render (request, 'agg_pro.html', {'formulario':formulario})
    

#vendedor
def vende(request):
    vend = Vendedor.objects.all()
    context = {'vend':vend}
    return render (request, 'vendedor.html',context )

def ggven (request):
    if request.method == 'POST':
        formulario = vendedorf  (request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('vende')
    else:
        formulario = vendedorf ()
        return render (request, 'agg_ven.html', {'formulario':formulario})
# Create your views here.
