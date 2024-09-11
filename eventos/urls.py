from django.urls import path
from . import views


app_name = 'eventos'
urlpatterns = [path("", views.Home.as_view(), name="home"),
               path("crear_evento", views.CrearEvento.as_view(), name="crear_evento"),
]