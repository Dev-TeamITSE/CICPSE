from django.urls import path
from . import views

app_name = 'ficha_antropologia'

urlpatterns = [
    path('formAntropologia/', views.formAntropologia, name='formAntropologia'),
    path('ficha/', views.ficha, name='ficha'),
    path('ficha/<int:nro_id>/', views.ficha_detalle, name='ficha_detalle'),
    ]