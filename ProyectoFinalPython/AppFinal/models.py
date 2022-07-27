from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=40)
    precio = models.FloatField()
    SKU = models.CharField(max_length=30, unique=True)
    stock = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='producto_image', default='coca.png')

class Cliente(models.Model):
    #user = 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    mail = models.EmailField()
    contraseña = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

class Comentarios(models.Model):

    opciones = ( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
    ("6", "6"), 
    ("7", "7"), 
    ("8", "8"), 
    ("9", "9"),
    ("10", "10"),
    ) 
    comentario = models.TextField()
    puntuacion = models.CharField(default=1, choices=opciones, max_length=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)