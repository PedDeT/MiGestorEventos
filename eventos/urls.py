from django.urls import path
from . import views


app_name = 'eventos'
urlpatterns = [path("", views.Home.as_view(), name="home"),
               path("crear_evento/", views.CrearEvento.as_view(), name="crear_evento"),
               path('editar_evento/<int:pk>/', views.EditarEvento.as_view(), name='editar_evento'),
               path('eliminar_evento/<int:pk>/', views.EliminarEvento.as_view(), name='eliminar_evento'),
               path('organizadores/', views.Organizadores.as_view(), name='organizadores'),
]