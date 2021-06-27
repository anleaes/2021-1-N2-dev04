from django.urls import path
from . import views

app_name = 'ministered_medicines'

urlpatterns = [
    path('', views.list_ministered_medicines, name='list_ministered_medicines'),
    path('adicionar/<int:id_patient>/', views.add_ministered_medicines, name='add_ministered_medicines'),
    path('excluir/<int:id_ministered_medicines>/', views.delete_ministered_medicines, name='delete_ministered_medicines'),
    path('excluir-item/<int:id_ministered_medicines_item>/', views.delete_ministered_medicines_item, name='delete_ministered_medicines_item'),
    path('adicionar-item/<int:id_ministered_medicines>/', views.add_ministered_medicines_item, name='add_ministered_medicines_item'),
    path('editar-status/<int:id_ministered_medicines>/', views.edit_ministered_medicines_status, name='edit_ministered_medicines_status'),
]
