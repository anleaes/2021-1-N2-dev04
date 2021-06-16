from django.urls import path
from . import views

app_name = 'health_professionals'

urlpatterns = [
    path('', views.list_health_professionals, name='list_health_professionals'),
    path('adicionar/', views.add_health_professionals, name='add_health_professionals'),
    path('editar/<int:id_health_professionals>/', views.edit_health_professionals, name='edit_health_professionals'),
    path('excluir/<int:id_health_professionals>/', views.delete_health_professionals, name='delete_health_professionals'),
]