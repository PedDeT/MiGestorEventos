from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, FormView


from .forms import EventoForm
from .models import Evento

# Create your views here.

class Home(ListView):
    model = Evento
    template_name = 'eventos/home.html'


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
    template_name = 'eventos/actualizar_evento.html'

