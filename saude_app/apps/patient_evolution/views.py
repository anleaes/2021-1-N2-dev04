from django.shortcuts import render
from .models import PatientEvolution, Patient, Anamnesis, VitalSign
from .forms import PatientEvolutionForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/autenticacao/login/')
def list_patient_evolution(request, id_patient):
    template_name = 'patient_evolution/list_patient_evolution.html'
    patients = Patient.objects.get(id=id_patient)
    anamnesis = Anamnesis.objects.filter(patients_id=id_patient)
    vital_signs = VitalSign.objects.filter(patient_id=id_patient)
    context = {
        'patients':patients,
        'anamnesis': anamnesis,
        'vital_signs': vital_signs,
    }
    return render(request,template_name, context)
