from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name = "home" ),
    path('clientes/', cliente, name = "clientes" ),
    path('empleados/', empleado, name = "empleados" ),
    path('productos/', productos, name = "productos" ),
    path('proveedores/', proveedores, name = "proveedores" ),

     path('buscar_cliente/', buscarCliente, name="buscar_cliente"),
     path('buscar2/', buscar2, name="buscar2"),

     #path('cliente_form/', clienteForm, name="cliente_form"),
    
     path('create_empleado/', EmpleadoCreate.as_view(), name="create_empleado" ),    
     path('update_empleado/<int:pk>/', EmpleadoUpdate.as_view(), name="update_empleado"),
     path('delete_empleado/<int:pk>/', EmpleadoDelete.as_view(), name="delete_empleado"),

     path('create_producto/', ProductosCreate.as_view(), name="create_productos" ),    
     path('update_producto/<int:pk>/', ProductosUpdate.as_view(), name="update_productos"),
     path('delete_producto/<int:pk>/', ProductosDelete.as_view(), name="delete_productos"),

     path('create_proveedor/', ProveedoresCreate.as_view(), name="create_proveedores" ),    
     path('update_proveedor/<int:pk>/', ProveedoresUpdate.as_view(), name="update_proveedores"),
     path('delete_proveedor/<int:pk>/', ProveedoresDelete.as_view(), name="delete_proveedores"),

     path('create_cliente/', ClienteCreate.as_view(), name="create_clientes" ),    
     path('update_cliente/<int:pk>/', ClienteUpdate.as_view(), name="update_clientes"),
     path('delete_cliente/<int:pk>/', ClienteDelete.as_view(), name="delete_clientes"),

     path('login/', login_request, name="login" ),
     path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
     path('registro/', register, name="registro" ),
     path('editar_perfil/', editarPerfil, name="editar_perfil" ),
     path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),

     path('acerca_de_mi/', acercaDeMi, name="acerca_de_mi" ),



    
]

