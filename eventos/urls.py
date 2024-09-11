from django.urls import path
from . import views


app_name = 'eventos'
urlpatterns = [path("", views.Home.as_view(), name="home"),
               path("crear_evento/", views.CrearEvento.as_view(), name="crear_evento"),
               path("editar_evento/", views.EditarEvento.as_view(), name="editar_evento"),
]