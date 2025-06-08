from django.shortcuts import render, get_object_or_404
from .models import Ficha

def formAntropologia(request):
    return render(request, 'formAntropologia.html')

def lista_fichas(request):
    fichas = Ficha.objects.order_by('nro_id')
    return render(request, 'antropologia.html', {'fichas': fichas})

def ficha_detalle(request, nro_id):
    ficha = get_object_or_404(Ficha, nro_id=nro_id)
    return render(request, 'ficha_detalle.html', {'ficha': ficha})
