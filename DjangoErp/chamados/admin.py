from django.contrib import admin
from .models import Tecnico, Chamados, Status
# Register your models here.

admin.site.register(Chamados)
admin.site.register(Tecnico)
admin.site.register(Status)

