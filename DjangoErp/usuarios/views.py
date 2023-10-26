from django.views.generic.edit import CreateView, UpdateView
from .forms import UsuarioForm
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Empresa


class UsuarioCreate(CreateView):
    template_name = "usuarios/cadastro.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='master')
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()

        Empresa.objects.create(user_master=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Usuário"
        context['botao'] = "Registrar"

        return context


class EmpresaUpdate(UpdateView):
    template_name = 'usuarios/empresa.html'
    model = Empresa
    fields = ['nome_fantasia', 'razao_social', 'endereco', 'numero', 'cidade', 'cep']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Empresa, user_master=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['Titulo'] = 'Crie sua Empresa'
        context['botao'] = 'Criar'

        return context
