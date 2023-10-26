from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Lista
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django .shortcuts import get_object_or_404


# create
class ListaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Lista.objects.using('second_db').all()
    fields = ['produto', 'recebido', 'pessoa']
    template_name = 'cadastros/form-etiqueta.html'
    success_url = reverse_lazy('listar-lista')

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
class ListaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Lista.objects.using('second_db').all()
    fields = ['produto', 'recebido', 'pessoa']
    template_name = 'cadastros/form-etiqueta.html'
    success_url = reverse_lazy('listar-lista')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Lista.objects.using('second_db').all(), pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Produto"
        context['botao'] = "Atualizar"
        return context


# Delete
class ListaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Lista.objects.using('second_db').all()
    template_name = 'cadastros/form-excluir-listar-manuais-cliente.html'
    success_url = reverse_lazy('listar-lista')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Lista.objects.using('second_db').all(), pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


# View
class ListaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Lista.objects.using('second_db').all()
    template_name = 'cadastros/listas/listar-manuais-cliente.html'

    # Parametro que permite que o usuario veja apenas seus campos
    def get_queryset(self):
        self.object_list = Lista.objects.filter(usuario=self.request.user)
        return self.object_list


