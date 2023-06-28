from django.shortcuts import render,HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from AppRegistros.forms import clienteFormulario,vendedorFormulario,articulosFormulario
from AppRegistros.models import Cliente,Vendedor,Articulos

def inicio(request):
    return render(request,"Plantillas/inicio.html")

# def clientes(request):
#   return render(request,"Plantillas/clientes.html")

def vendedores(request):
    if request.method=='POST':
        miFormulario=vendedorFormulario(request.POST) #aquí mellega toda la información del html
        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            cliente = Vendedor(razon_social=informacion['razon_social'], cuit=informacion['cuit'], telefono=informacion['telefono']) 

            cliente.save()

            return render(request, "Plantillas/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 
        miFormulario= vendedorFormulario() #Formulario vacio para construir el html

    return render(request, "Plantillas/vendedores.html", {"miFormulario":miFormulario})

def articulos(request):
    if request.method=='POST':
        miFormulario=articulosFormulario(request.POST) #aquí mellega toda la información del html
        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            cliente = Articulos(nombre=informacion['nombre'], precio=informacion['precio'], rubro=informacion['rubro']) 

            cliente.save()

            return render(request, "Plantillas/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 
        miFormulario= articulosFormulario() #Formulario vacio para construir el html

    return render(request, "Plantillas/articulos.html", {"miFormulario":miFormulario})

def clientes(request):
    if request.method=='POST':
        miFormulario=clienteFormulario(request.POST) #aquí mellega toda la información del html
        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], telefono=informacion['telefono']) 

            cliente.save()

            return render(request, "Plantillas/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 
        miFormulario= clienteFormulario() #Formulario vacio para construir el html

    return render(request, "Plantillas/clientes.html", {"miFormulario":miFormulario})

def BusquedaArticulos(request):
    return render(request,"Plantillas/busquedaArticulos.html")

def buscar(request):            
    if request.GET["nombre"]:
        nombre = request.GET['nombre'] 
        articulo = Articulos.objects.filter(nombre=nombre)
        return render(request, "Plantillas/resultadosBusqueda.html", {"articulo":articulo, "nombre":nombre})
    else: 
        respuesta="Error.Articulo no encontrado"
    return render(request,"Plantillas/busquedaArticulos.html",{"respuesta":respuesta})
    
    