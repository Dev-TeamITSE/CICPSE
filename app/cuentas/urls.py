from django.urls import path
from . import views

app_name = 'cuentas'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'), 
    path('colecciones/', views.colecciones, name='colecciones'),  # 📌 Página de colecciones
    path('register/', views.register, name='register'), 
    path('users/',views.users, name='users'),  
    path("admit_user/<int:user_id>/", views.admit_user, name="admit_user"),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path("edit_user/<int:user_id>/", views.edit_user, name="edit_user"),
    path('update_password/', views.update_password, name='update_password'),
    path('news/', views.noticias_view, name='news'),  # 📌 Página donde se mostrarán las noticias
    path('cargar_noticias/', views.cargar_noticias_view, name='cargar_noticias'),  # 📌 Formulario de carga de noticias
    path('api/noticias/', views.obtener_noticias, name='obtener_noticias'),
    path('bellas_artes/', views.bellas_artes, name='bellas_artes'),
    path('historia/', views.historia, name='historia'),
    path('antropologia/', views.antropologia, name='antropologia'),
    path('formularioAntropologia/', views.formularioAntropologia, name='formularioAntropologia'),
    path('<str:area>/crear_coleccion/', views.crear_coleccion, name='crear_coleccion'),
    path('coleccion/<int:pk>/', views.detalle_coleccion, name='detalle_coleccion'),
    path('coleccion/<int:pk>/borrar/', views.borrar_coleccion, name='borrar_coleccion'),
    path('ajax/toggle_privacidad/', views.toggle_privacidad_ajax, name='toggle_privacidad_ajax'),
    path('<str:area>/crear_coleccion/', views.crear_coleccion, name='crear_coleccion'),


    



    ]