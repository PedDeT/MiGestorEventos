from django.urls import path
from . import views


urlpatterns = [
    path("", views.VistaListaEventos.as_view(), name="lista_eventos"),
    path("organizador/", views.VistaListaOrganizador.as_view(), name="lista_organizador"),
    path("organizador/new/", views.VistaCrearOrganizador.as_view(), name="crear_organizador"),
    path("evento/<int:pk>/edit/", views.VistaEditarEvento.as_view(), name="editar_evento"),
]