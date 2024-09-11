from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ["nombre", "organizador"]

    def limpiar_nombre(self):
        nombre = self.cleaned_data['nombre']
        if 'Cancelado' in nombre:
            raise forms.ValidationError("El nombre del evento no es válido")
        return nombre

