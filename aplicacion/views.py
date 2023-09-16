from django.shortcuts import render
from .models import Cliente, Empleado, Productos, Proveedores, Avatar
from django.urls import reverse_lazy

from .forms import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

@login_required
def cliente(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes, 'titulo': 'Listado de Clientes'}
    return render(request, 'aplicacion/clientes.html', contexto)

@login_required
def empleado(request):
    empleados = Empleado.objects.all()
    contexto = {'empleados': empleados}
    return render(request, 'aplicacion/empleados.html', contexto)

@login_required
def productos(request):
    productos = Productos.objects.all()
    contexto = {'productos': productos}
    return render(request, 'aplicacion/productos.html', contexto)

@login_required
def proveedores(request):
    proveedores = Proveedores.objects.all()
    contexto = {'proveedores': proveedores}
    return render(request, 'aplicacion/proveedores.html', contexto)


#Buscar Clientes (Search)
@login_required
def buscarCliente(request):
    return render(request, "aplicacion/buscarCliente.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        cliente = Cliente.objects.filter(nombre_empresa__icontains=patron)
        contexto = {'clientes': cliente} 
        return render(request, "aplicacion/clientes.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#Agregar Clientes
@login_required
def clienteForm(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            nombre_empresa = form.cleaned_data.get('nombreApellido')
            telefono_contacto = form.cleaned_data.get('telefono_contacto')
            direccion = form.cleaned_data.get('direccion')
            email = form.cleaned_data.get('email')
            cliente = Cliente(nombre_empresa=nombre_empresa, telefono_contacto=telefono_contacto, direccion=direccion, email=email)
            cliente.save()
            return render(request, "aplicacion/base.html")  
    else:
        form = ClienteForm()
    
    return render(request, "aplicacion/clienteForm.html", {"form": form})


#Crear, Modificar y Eliminar
class EmpleadoList(LoginRequiredMixin, ListView):
    model = Empleado

class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = Empleado
    fields = ['nombreApellido', 'direccion', 'telefono_contacto', 'cargo', 'fecha_alta']
    success_url = reverse_lazy('empleados')    

class EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    model = Empleado
    fields = ['nombreApellido', 'direccion', 'telefono_contacto', 'cargo', 'fecha_alta']
    success_url = reverse_lazy('empleados')

class EmpleadoDelete(LoginRequiredMixin, DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

#Crear, Modificar y Eliminar
class ProductosList(LoginRequiredMixin, ListView):
    model = Productos

class ProductosCreate(LoginRequiredMixin, CreateView):
    model = Productos
    fields = ['modelo', 'color', 'material', 'cantidad']
    success_url = reverse_lazy('productos')    

class ProductosUpdate(LoginRequiredMixin, UpdateView):
    model = Productos
    fields = ['modelo', 'color', 'material', 'cantidad']
    success_url = reverse_lazy('productos')

class ProductosDelete(LoginRequiredMixin, DeleteView):
    model = Productos
    success_url = reverse_lazy('productos')

#Crear, Modificar y Eliminar
class ProveedoresList(LoginRequiredMixin, ListView):
    model = Proveedores

class ProveedoresCreate(LoginRequiredMixin, CreateView):
    model = Proveedores
    fields = ['nombre_empresa', 'vendedor', 'telefono_contacto', 'direccion', 'email']
    success_url = reverse_lazy('proveedores')    

class ProveedoresUpdate(LoginRequiredMixin, UpdateView):
    model = Proveedores
    fields = ['nombre_empresa', 'vendedor', 'telefono_contacto', 'direccion', 'email']
    success_url = reverse_lazy('proveedores')

class ProveedoresDelete(LoginRequiredMixin, DeleteView):
    model = Proveedores
    success_url = reverse_lazy('proveedores')

#Crear, Modificar y Eliminar
class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre_empresa', 'telefono_contacto', 'direccion', 'email']
    success_url = reverse_lazy('clientes')    

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre_empresa', 'telefono_contacto', 'direccion', 'email']
    success_url = reverse_lazy('clientes')

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')


##Login/logout

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm}) 


#Registro de usuario


def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

#Editar perfil

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/base.html")
        else:
            return render(request,"aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

#Agregar Avatar

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })

##Acerca de mi

def acercaDeMi(request):
    return render(request, 'aplicacion/acercaDeMi.html', {})
