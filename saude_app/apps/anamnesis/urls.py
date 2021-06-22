from django.urls import path
from . import views

app_name = 'anamnesis'

urlpatterns = [
    path('', views.list_anamnesis, name='list_anamnesis'),
    path('adicionar/', views.add_anamnesis, name='add_anamnesis'),
    path('editar/<int:id_anamnesis>/', views.edit_anamnesis, name='edit_anamnesis'),
    path('excluir/<int:id_anamnesis>/', views.delete_anamnesis, name='delete_anamnesis'),
]
