from django.urls import path
from .views import ChamadoCreate
from .views import ChamadoUpdate
from .views import ChamadoDelete
from .views import ChamadoList
from .views import ChamadosAdmin
from .views import ChamadosClienteList

urlpatterns = [
    path('cadastrar/chamado/', ChamadoCreate.as_view(), name='cadastrar-chamado'),

    path(f'editar/chamado/<int:pk>/', ChamadoUpdate.as_view(), name='editar-chamado'),

    path(f'excluir/chamado/<int:pk>/', ChamadoDelete.as_view(), name='excluir-chamado'),

    path(f'listar/chamados/', ChamadoList.as_view(), name='listar-chamados'),

    path(f'listar/chamados/admin', ChamadosAdmin.as_view(), name='listar-chamados-admin'),

    path(f'listar/chamados/cliente/<int:pk>/', ChamadosClienteList.as_view(), name='listar-chamados-cliente'),

]