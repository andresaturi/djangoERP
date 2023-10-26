from django.urls import path
from .views import ListaCreate
from .views import ListaUpdate
from .views import ListaDelete
from .views import ListaList

urlpatterns = [
    path('cadastrar/lista/', ListaCreate.as_view(), name='cadastrar-lista'),

    path(f'editar/lista/<int:pk>/', ListaUpdate.as_view(), name='editar-lista'),

    path(f'excluir/lista/<int:pk>/', ListaDelete.as_view(), name='excluir-lista'),

    path(f'listar/lista/', ListaList.as_view(), name='listar-lista'),

]