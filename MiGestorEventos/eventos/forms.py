from django import forms
from .models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'lugar']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if 'Cancelado' in nombre:
            raise forms.ValidationError("Nombre inválido. El nombre no puede tener la palabra 'Cancelado'.")
        return nombre
