from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="index"),
    path("procesar_votos", views.procesar_formulario, name="procesar_votos")
]