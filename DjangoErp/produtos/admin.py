from django.contrib import admin
from .models import Produto, CFOP, Categoria, SitTributaria
# Register your models here.

admin.site.register(Produto)
admin.site.register(CFOP)
admin.site.register(Categoria)
admin.site.register(SitTributaria)


