from django.shortcuts import render, HttpResponseRedirect
from django.db import transaction
from django.db import models

from .models import Lenguaje
# Create your views here.


def procesar_formulario(request):
    if request.method == 'POST':
        # Obtener los lenguajes seleccionados como lista de IDs
        lenguajes_seleccionados = [int(id) for id in request.POST.getlist('lenguajes')]

        # Actualizar los votos de cada lenguaje seleccionado
        for lenguaje_id in lenguajes_seleccionados:
            try:
                lenguaje = Lenguaje.objects.get(id=lenguaje_id)
                lenguaje.votos += 1
                lenguaje.save()
            except Lenguaje.DoesNotExist:
                # Manejar el caso de que un lenguaje no exista
                pass

        # Redireccionar a la página principal (index.html)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def index(request):

    # Obtener todos los lenguajes y sus votos
    lenguajes = Lenguaje.objects.all()

    # Calcular los porcentajes de votos
    total_votos = sum(lenguaje.votos for lenguaje in lenguajes)
    for lenguaje in lenguajes:
        try:
            lenguaje.porcentaje = (lenguaje.votos / total_votos) * 100
        except ZeroDivisionError:
            lenguaje.porcentaje = 0  # Asignar 0 en caso de error

    # Preparar el contexto para la plantilla
    contexto = {
        'lenguajes': lenguajes,
    }

    # Renderizar la plantilla index.html
    return render(request, 'index.html', contexto)