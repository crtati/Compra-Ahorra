from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=30,primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    password = models.CharField(max_length=200)

class Login(models.Model):
    nombreUsuario = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=200)

class Producto(models.Model):
    codigo_producto = models.CharField(max_length=30,primary_key=True)
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    stock = models.CharField(max_length=30)

class Carrito(models.Model):
    id_product = models.CharField(max_length=30,primary_key=True)
    nombreProducto = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    total = models.CharField(max_length=30)

class Venta(models.Model):
    id_venta = models.CharField(max_length=4, primary_key=True)
    fecha = models.CharField(max_length=20)
    estado = models.CharField(max_length=30)
    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

class Promocion(models.Model):
    nombreUsuario = models.CharField(max_length=30)

class Suscripcion(models.Model):
    id_donacion = models.CharField(max_length=4, primary_key=True)
    monto = models.CharField(max_length=30)
    fecha = models.CharField(max_length=30)
    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

class UsuarioProducto(models.Model):
    nombreUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    codigo_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    cantidad = models.CharField(max_length=30)

