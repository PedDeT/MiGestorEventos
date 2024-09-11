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
    class Meta:
        model = Evento
        fields = ["nombre", "lugar", "fecha"]

    def limpiar_nombre(self):
        nombre = self.cleaned_data['nombre']
        if 'Cancelado' in nombre:
            raise forms.ValidationError("El nombre del evento no es válido")
        return nombre


