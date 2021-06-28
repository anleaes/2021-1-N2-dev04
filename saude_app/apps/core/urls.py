from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/', views.search_clients, name='search_patients'),
    #path('ver/<int:id_patient>/', views.edit_client, name='ver_patient'),    
]
