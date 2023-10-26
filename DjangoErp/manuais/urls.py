from django.urls import path
from .views import ManualCreate
from .views import ManualUpdate
from .views import ManualDelete
from .views import ManualList
from .views import ManualClienteList

urlpatterns = [
    path('cadastrar/manual/', ManualCreate.as_view(), name='cadastrar-manual'),

    path(f'editar/manual/<int:pk>/', ManualUpdate.as_view(), name='editar-manual'),

    path(f'excluir/manual/<int:pk>/', ManualDelete.as_view(), name='excluir-manual'),

    path(f'listar/manual/', ManualList.as_view(), name='listar-manuais'),

    path(f'listar/manual/cliente/<int:pk>/', ManualClienteList.as_view(), name='listar-manuais-cliente')
]