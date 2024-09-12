from django import forms
from allauth.account.forms import SignupForm


from .models import Evento

class CustomSignupForm(SignupForm):
    nombre = forms.CharField(label='Nombre', max_length=100, required=True)

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields.move_to_end('nombre', last=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.nombre = self.cleaned_data['nombre']
        user.save()
        return user

class EventoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the user from kwargs
        super().__init__(*args, **kwargs)

    class Meta:
        model = Evento
        fields = ["nombre", "lugar", "fecha"]

    def limpiar_nombre(self):
        nombre = self.cleaned_data['nombre']
        if 'Cancelado' in nombre:
            raise forms.ValidationError("El nombre del evento no es válido")
        return nombre

    def save(self, commit=True):
        evento = super().save(commit=False)
        if self.user:
            evento.organizador = self.user  # Set the current user as the organizer
        if commit:
            evento.save()
        return evento

class EliminarEventoForm(forms.Form):
    confirm_delete = forms.BooleanField(label="Confirmar que desea eliminar el evento")
