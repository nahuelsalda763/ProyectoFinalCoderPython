from django.db import models

# Create your models here.

from http import client
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length= 40)
    price = models.FloatField()
    desc = models.TextField()
    SKU = models.CharField(max_length=30)
    stock = models.BooleanField(default= True)
    image = models.ImageField(upload_to='producto_image', default='producto_image/descarga.png')
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)
   
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length= 40, default= "client")
    email = models.EmailField()
    first_name =  models.CharField(max_length= 40)
    last_name =  models.CharField(max_length= 40)

class Comment(models.Model):

    commentoptions = ( 
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
    comments = models.TextField()
    punctuation = models.CharField(default=1, choices=commentoptions, max_length=2)
    name = models.CharField(max_length=40)
  
    class Meta:
        verbose_name = 'coment'
        verbose_name_plural = 'comentarios'