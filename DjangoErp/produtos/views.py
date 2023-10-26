from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Categoria, CFOP, SitTributaria, Produto
from django.utils import timezone
from django import forms
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


# create
class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = U"restaurante"
    model = Produto
    fields = ['nome', 'foto', 'descricao', 'categoria', 'custo', 'venda', 'CFOP', 'ncm', 'sit_tributaria']
    template_name = 'cadastros/form-produtos.html'
    success_url = reverse_lazy('listar-produtos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar um novo Produto"
        context['botao'] = "Cadastrar"
        return context


# Update
class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = U"restaurante"
    model = Produto
    fields = ['nome', 'foto', 'descricao', 'ativo', 'categoria', 'custo', 'venda', 'ncm', 'sit_tributaria']
    template_name = 'cadastros/form-produtos.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Produto"
        context['botao'] = "Atualizar"
        return context


# Atualiza o produto para inativo, não o exclui
class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Produto
    template_name = 'cadastros/form-excluir-produto.html'
    success_url = reverse_lazy('listar-produtos')


# View
class ProdutoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = U"restaurante"
    model = Produto
    template_name = 'cadastros/listas/listar-produtos.html'
    paginate_by = 30

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.GET.get('nome')

        if busca:
            queryset = Produto.objects.filter(nome__icontains=busca)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProdutoView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/listas/listar-produto-cliente.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        self.object_list = get_object_or_404(Produto, pk=pk)
        return self.object_list








