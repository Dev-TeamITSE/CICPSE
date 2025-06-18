from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Ficha

def formAntropologia(request):
    return render(request, 'formAntropologia.html')

def ficha(request):
    fichas = Ficha.objects.filter(nro_id__isnull=False).order_by('nro_id')
    paginator = Paginator(fichas, 10)
    page = request.GET.get('page')
    fichas_paginadas = paginator.get_page(page)
    return render(request, 'ficha.html', {'fichas': fichas_paginadas})

def ficha_detalle(request, nro_id):
    ficha = get_object_or_404(Ficha, nro_id=nro_id)
    return render(request, 'ficha_detalle.html', {'ficha': ficha})
