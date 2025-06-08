from django.urls import path
from . import views

app_name = 'ficha_antropologia'

urlpatterns = [
    path('formAntropologia/', views.formAntropologia, name='formAntropologia'),
    path('fichas/', views.lista_fichas, name='lista_fichas'),
    path('ficha/<int:nro_id>/', views.ficha_detalle, name='ficha_detalle'),
    ]