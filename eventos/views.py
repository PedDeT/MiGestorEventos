from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView

from .forms import EventoForm
from .models import Evento
from .models import Organizador

# Create your views here.

class VistaListaEventos(ListView):
    model = Evento
    template_name = 'eventos/lista_eventos.html'

class VistaCrearEventos(CreateView):
    model = Evento
    template_name = 'eventos/crear_evento.html'
    success_url = '/'

class VistaListaOrganizador(ListView):
    model = Organizador
    template_name = 'eventos/lista_organizador.html'

class VistaCrearOrganizador(CreateView):
    model = Organizador
    fields = ['nombre']
    template_name = 'eventos/crear_organizador.html'
    success_url = '/organizador/'

@method_decorator(login_required, name='dispatch')
class VistaEditarEvento(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/actualizar_evento.html'