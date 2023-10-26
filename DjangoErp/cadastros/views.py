from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Campo, Atividade
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#from braces.views import GroupRequiredMixin
from django .shortcuts import get_object_or_404


# create
class CampoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form-etiqueta.html'
    success_url = reverse_lazy('listarr-campo')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar um novo Campo"
        context['botao'] = "Cadastrar"
        return context


class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo', 'arquivo']
    template_name = 'cadastros/form-listar-etiqueta.html'

    success_url = reverse_lazy('listar-atividade')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar uma nova Atividade"
        context['botao'] = "Cadastrar"
        return context


# Update
class CampoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form-etiqueta.html'
    success_url = reverse_lazy('listar-campo')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campo, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Campo"
        context['botao'] = "Atualizar"
        return context


class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo', 'arquivo']
    template_name = 'cadastros/form-listar-etiqueta.html'
    success_url = reverse_lazy('listar-atividade')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Atividade"
        context['botao'] = "Atualizar"
        return context


# Delete
class CampoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Campo
    template_name = 'cadastros/form-excluir-listar-manuais-cliente.html'
    success_url = reverse_lazy('listar-campo')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campo, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class AtividadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir-listar-etiqueta.html'
    success_url = reverse_lazy('listar-atividade')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


# View
class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/listar-manuais-cliente.html'

    # Parametro que permite que o usuario veja apenas seus campos
    def get_queryset(self):
        self.object_list = Campo.objects.filter(usuario=self.request.user)
        return self.object_list


class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/listar-etiqueta.html'

    def get_queryset(self):
        self.object_list = Atividade.objects.filter(usuario=self.request.user)
        return self.object_list