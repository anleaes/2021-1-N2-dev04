from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnamnesisForm
from .models import Anamnesis, Patient, HealthProfessional


def add_anamnesis(request):
    template_name = 'anamnesis/add_anamnesis.html'
    context = {}
    if request.method == 'POST':
        form = AnamnesisForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.health_professional = Client.objects.get(id=id_health_professional)
            f.patient = Patient.objects.get(id=id_patient)
            f.save()
            form.save_m2m()
            return redirect('anamnesis:list_anamnesis')
    form = AnamnesisForm()
    context['form'] = form
    return render(request, template_name, context)

def list_anamnesis(request):
    template_name = 'anamnesis/list_anamnesis.html'
    anamnesis = Anamnesis.objects.filter()
    health_professionals = HealthProfessional.objects.filter()
    patients = Patient.objects.filter()
    context = {
        'anamnesis': anamnesis,
        'health_professionals': health_professionals,
        'patients': patients
    }
    return render(request, template_name, context)

def edit_anamnesis(request, id_anamnesis):
    template_name = 'anamnesis/add_anamnesis.html'
    context ={}
    anamnesis = get_object_or_404(Anamnesis, id=id_anamnesis)
    if request.method == 'POST':
        form = AnamnesisForm(request.POST, instance=anamnesis)
        if form.is_valid():
            form.save()
            return redirect('anamnesis:list_anamnesis')
    form = AnamnesisForm(instance=anamnesis)
    context['form'] = form
    return render(request, template_name, context)

def delete_anamnesis(request, id_anamnesis):
    anamnesis = Anamnesis.objects.get(id=id_anamnesis)
    anamnesis.delete()
    return redirect('anamnesis:list_anamnesis')
