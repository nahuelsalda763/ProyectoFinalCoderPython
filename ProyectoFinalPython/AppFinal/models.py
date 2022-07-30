from http import client
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    SKU = models.CharField(max_length=30, unique=True)
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='producto_image', default='producto_image/descarga.png')

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length= 40, default= "client", editable = False)
    email = models.EmailField()
    first_name =  models.CharField(max_length= 40)
    last_name =  models.CharField(max_length= 40)

class Coments(models.Model):

    comentoptions = ( 
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
    coments = models.TextField()
    puntuation = models.CharField(default=1, choices=comentoptions, max_length=2)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

"""class WishList(models.Model):
    user = models.OneToOneField(User)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        db_table = 'shop_wishlist'
        verbose_name = _('Wishlist')

class WishlistItem(models.Model):

    wishlist = models.ForeignKey(Wishlist)
    product = models.ForeignKey(Product)"""