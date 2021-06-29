from django.urls import path
from . import views

app_name = 'patient_evolution'

urlpatterns = [
    path('evolucao-paciente/<int:id_patient>/', views.list_patient_evolution, name='list_patient_evolution'),
]