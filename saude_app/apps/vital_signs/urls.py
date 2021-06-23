
from django.urls import path
from . import views

app_name = 'vital_signs'

urlpatterns = [
    path('', views.list_vital_signs, name='list_vital_signs'),
    path('adicionar/', views.add_vital_sign, name='add_vital_sign'),
    path('excluir/<int:id_vital_signs>/', views.delete_vital_sign, name='delete_vital_sign'),
]

