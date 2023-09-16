from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    direccion = models.CharField (max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre_empresa} - ({self.telefono_contacto}) - ({self.direccion}) - ({self.email})"
    

class Empleado(models.Model):
    nombreApellido = models.CharField(max_length=100)
    direccion = models.CharField (max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    fecha_alta = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombreApellido} - ({self.direccion}) - ({self.telefono_contacto}) - ({self.cargo}) - ({self.fecha_alta})"
    

class Productos(models.Model):
    modelo = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    cantidad = models.IntegerField() 

    def __str__(self):
        return f"{self.modelo} - ({self.color}) - ({self.material}) - ({self.cantidad})"
    
class Proveedores(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    vendedor = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    direccion = models.CharField (max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre_empresa} - ({self.vendedor}) - ({self.telefono_contacto}) - ({self.direccion}) - ({self.email})"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"