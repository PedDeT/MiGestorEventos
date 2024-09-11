from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from .forms import EventoForm
from .models import Evento

# Create your views here.

class Home(ListView):
    model = Evento
    template_name = 'eventos/home.html'

class CrearEvento(CreateView):
    model = Evento
    template_name = 'eventos/crear_evento.html'
    success_url = '/'

@method_decorator(login_required, name='dispatch')
class VistaEditarEvento(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/actualizar_evento.html'