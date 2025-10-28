from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_voluntarios/', views.lista_voluntarios, name='lista_voluntarios'),
    path('crear_voluntario/', views.crear_voluntario, name='crear_voluntario'),
    path('voluntarios/<int:voluntario_id>/', views.detalle_voluntario, name='detalle_voluntario'),
    path('actualizar_voluntario/<int:voluntario_id>/', views.actualizar_voluntario, name='actualizar_voluntario'),
    path('eliminar_voluntario/<int:voluntario_id>/', views.voluntario_delete, name='voluntario_delete'),
    path('lista_eventos/', views.lista_eventos, name='lista_eventos'),
    path('crear_evento/', views.crear_evento, name='crear_evento'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('actualizar_evento/<int:evento_id>/', views.actualizar_evento, name='actualizar_evento'),
    path('eliminar_evento/<int:evento_id>/', views.evento_delete, name='evento_delete'),
]