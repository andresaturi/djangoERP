from django.urls import path
from .views import CampoCreate, AtividadeCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoDelete, AtividadeDelete
from .views import CampoList, AtividadeList

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),

    path(f'editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path(f'editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),

    path(f'excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path(f'excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),

    path(f'listar/campos/', CampoList.as_view(), name='listar-campo'),
    path(f'listar/atividades/', AtividadeList.as_view(), name='listar-atividade')
]