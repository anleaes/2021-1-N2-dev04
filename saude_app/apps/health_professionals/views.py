from django.shortcuts import render, get_object_or_404, redirect
from .forms import HealthProfessionalsForm
from .models import health_professionals

# Create your views here.

def add_health_professionals(request):
    template_name = 'health_professionals/add_health_professionals.html'
    context = {}
    if request.method == 'POST':
        form = HealthProfessionalsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('clients:list_clients')
    form = HealthProfessionalsForm()
    context['form'] = form
    return render(request, template_name, context)
def list_health_professionals(request):
    template_name = 'health_professionals/list_health_professionals.html'
    health_professionals = health_professionals.objects.filter()
    context = {
        'health_professionals': health_professionals
    }
    return render(request, template_name, context)

def edit_health_professionals(request, id_health_professionals):
    template_name = 'health_professionals/add_health_professionals.html'
    context ={}
    health_professionals = get_object_or_404(health_professionals, id=id_health_professionals)
    if request.method == 'POST':
        form = HealthProfessionalsForm(request.POST, instance=health_professionals)
        if form.is_valid():
            form.save()
            return redirect('clients:list_health_professionals')
    form = HealthProfessionalsForm(instance=health_professionals)
    context['form'] = form
    return render(request, template_name, context)

def delete_health_professionals(request, id_health_professionals):
    health_professionals = health_professionals.objects.get(id=id_health_professionals)
    health_professionals.delete()
    return redirect('health_professionals:list_health_professionals')