from multiprocessing.connection import Client
from django.contrib import admin
from AppFinal.models import Product, Client
# Register your models here.

admin.site.register(Product)
admin.site.register(Client)