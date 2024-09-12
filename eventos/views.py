from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.shortcuts import get_object_or_404, redirect

from .forms import EventoForm, EliminarEventoForm
from .models import Evento, CustomUser

# Create your views here.

class Home(ListView):
    model = Evento
    template_name = 'eventos/home.html'

class Organizadores(ListView):
    model = CustomUser
    template_name = 'eventos/organizadores.html'


@method_decorator(login_required, name='dispatch')
class CrearEvento(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/crear_evento.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.organizador = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditarEvento(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/editar_evento.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.organizador = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EliminarEvento(FormView):
    template_name = 'eventos/eliminar_evento.html'
    form_class = EliminarEventoForm

    def form_valid(self, form):
        evento = get_object_or_404(Evento, pk=self.kwargs['pk'])
        if form.cleaned_data['confirm_delete']:
            evento.delete()
            return redirect('eventos:home')
        return super().form_invalid(form)