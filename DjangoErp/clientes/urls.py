from django.urls import path
from .views import ClienteCreate
from .views import ClienteUpdate
from .views import ClienteDelete
from .views import ClienteList
from .views import ClienteView


urlpatterns = [
    path('cadastrar/cliente/', ClienteCreate.as_view(), name='cadastrar-cliente'),

    path(f'editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name='editar-cliente'),

    path(f'excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name='excluir-cliente'),

    path(f'listar/cliente/', ClienteList.as_view(), name='listar-clientes'),

    path(f'listar/cliente/<int:pk>/', ClienteView.as_view(), name='listar-cliente'),

]