from django.urls import path
from .views import ProdutoCreate
from .views import ProdutoUpdate
from .views import ProdutoDelete
from .views import ProdutoList
#from .views import ProdutoAdmin
from .views import ProdutoView

urlpatterns = [
    path('cadastrar/produto/', ProdutoCreate.as_view(), name='cadastrar-produto'),

    path(f'editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name='editar-produto'),

    path(f'excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name='excluir-produto'),

    path(f'listar/produtos/', ProdutoList.as_view(), name='listar-produtos'),

    path(f'listar/produtos/cliente/<int:pk>/', ProdutoView.as_view(), name='listar-produto-cliente'),

]