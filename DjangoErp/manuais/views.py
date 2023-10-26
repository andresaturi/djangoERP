from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Manuais
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404


# create
class ManualCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Manuais
    fields = ['titulo', 'detalhes', 'arquivo']
    template_name = 'cadastros/form-manuais.html'
    success_url = reverse_lazy('listar-manuais')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar um novo Manual"
        context['botao'] = "Cadastrar"
        return context


# Update
class ManualUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Manuais
    fields = ['titulo', 'detalhes', 'arquivo']
    template_name = 'cadastros/form-manuais.html'
    success_url = reverse_lazy('listar-manuais')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Manual"
        context['botao'] = "Atualizar"
        return context


# Delete
class ManualDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Manuais
    template_name = 'cadastros/form-excluir-manual.html'
    success_url = reverse_lazy('listar-manuais')


# View
class ManualList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Manuais
    template_name = 'cadastros/listas/listar-manuais.html'


class ManualClienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Manuais
    template_name = 'cadastros/listas/listar-manuais-cliente.html'

    def manual_detail(self, pk):
        manual = get_object_or_404(Manuais, pk=pk)
        return render(self, 'cadastros/listas/listar-manuais-cliente.html', {'manual': manual})

        # Parametro que permite que o usuario veja apenas seus campos
    def get_queryset(self):
        pk = self.kwargs.get('pk')  # Certifique-se de obter a chave primária corretamente
        self.object_list = get_object_or_404(Manuais, pk=pk)
        return self.object_list








