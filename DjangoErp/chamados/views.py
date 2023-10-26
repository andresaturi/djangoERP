from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Tecnico, Status, Chamados
from django.utils import timezone
from django import forms
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


# create
class ChamadoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Chamados
    fields = ['empresa', 'assunto', 'contato', 'detalhes', 'arquivo']
    template_name = 'cadastros/form-chamados.html'
    success_url = reverse_lazy('listar-chamados')
    status = forms.CharField(initial='Aguardando Atend.')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.tecnico = Tecnico.objects.get(nome='Aguardando')
        form.instance.status = Status.objects.get(nome='Aguardando Atend.')
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar um novo Chamado"
        context['botao'] = "Cadastrar"
        return context


# Update
class ChamadoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Chamados
    fields = ['detalhes', 'arquivo', 'status', 'atividade', 'tecnico']
    template_name = 'cadastros/form-chamados.html'
    success_url = reverse_lazy('listar-chamados-admin')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Chamado"
        context['botao'] = "Atualizar"
        return context


# Atualiza o chamado para fechado, não o exclui
class ChamadoDelete(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Chamados
    fields = ['tecnico', 'resolucao']
    template_name = 'cadastros/form-excluir-chamado.html'
    success_url = reverse_lazy('listar-chamados-admin')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Manual"
        context['botao'] = "Atualizar"
        return context

    def form_valid(self, form):
        form.instance.status = Status.objects.get(nome='Fechado')
        form.instance.data_fechado = timezone.now()
        url = super().form_valid(form)
        return url


# View
class ChamadoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Chamados
    template_name = 'cadastros/listas/listar-chamados.html'

    def get_queryset(self):
        self.object_list = Chamados.objects.filter(usuario=self.request.user)
        return self.object_list


class FiltroForm(forms.Form):
    status = forms.ChoiceField(
        label='Status',
        choices=(
            ('', 'Abertos'),
            (1, 'Aguardando Atend.'),
            (3, 'Fechado'),
            (2, 'Em análise'),
        ),
        required=False,
    )


class ChamadosAdmin(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = U"Administrador"
    model = Chamados
    template_name = 'cadastros/listas/listar-chamados-admin.html'
    paginate_by = 30
    form_class = FiltroForm

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        busca = self.request.GET.get('empresa')

        if status:
            queryset = queryset.filter(status=status)
        else:
            queryset = queryset.exclude(status=3)

        if busca:
            queryset = Chamados.objects.filter(empresa__icontains=busca)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET)
        return context


class ChamadosClienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Chamados
    template_name = 'cadastros/listas/listar-chamados-cliente.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        self.object_list = get_object_or_404(Chamados, pk=pk)
        return self.object_list








