from django.contrib import admin
from .models import Cliente,Vendedor,Articulos
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Articulos)
