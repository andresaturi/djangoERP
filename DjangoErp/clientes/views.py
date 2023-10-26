from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Cliente
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# create
class ClienteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = U"restaurante"
    model = Cliente
    fields = ['nome', 'telefone', 'endereco', 'numero', 'cpf']
    template_name = 'cadastros/form-clientes.html'
    success_url = reverse_lazy('listar-clientes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar um novo Cliente"
        context['botao'] = "Cadastrar"
        return context


# Update
class ClienteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = U"restaurante"
    model = Cliente
    fields = ['nome', 'telefone', 'endereco', 'numero', 'cpf', 'ativo']
    template_name = 'cadastros/form-clientes.html'
    success_url = reverse_lazy('listar-clientes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Cliente"
        context['botao'] = "Atualizar"
        return context


# Delete
class ClienteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = U"restaurante"
    model = Cliente
    template_name = 'cadastros/form-excluir-cliente.html'
    success_url = reverse_lazy('listar-cliente')


# View
class ClienteListOld(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = U"restaurante"
    model = Cliente
    template_name = 'cadastros/listas/listar-clientes.html'


class ClienteView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = U"restaurante"
    model = Cliente
    template_name = 'cadastros/listas/cliente-view.html'


class ClienteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = U"restaurante"
    model = Cliente
    template_name = 'cadastros/listas/listar-clientes.html'
    paginate_by = 30

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.GET.get('nome')

        if busca:
            queryset = Cliente.objects.filter(nome__icontains=busca)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context











