from django.shortcuts import render, get_object_or_404, redirect
from .forms import MinisteredMedicinesForm, MinisteredMedicineItemForm
from .models import MinisteredMedicines , MinisteredMedicineItem, Patient, Medicine

# Create your views here.

def add_ministered_medicines(request, id_patient):
    template_name = 'ministered_medicines/add_ministered_medicines.html'
    context = {}
    if request.method == 'POST':
        form = MinisteredMedicinesForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.patient = Patient.objects.get(id=id_patient)
            f.save()
            form.save_m2m()
            return redirect('ministered_medicines:list_ministered_medicines')
    form = MinisteredMedicinesForm()
    context['form'] = form
    return render(request, template_name, context)

def list_ministered_medicines(request):
    template_name = 'ministered_medicines/list_ministered_medicines.html'
    ministered_medicines = MinisteredMedicines.objects.filter()
    ministered_medicines_items = MinisteredMedicineItem.objects.filter()
    patients = Patient.objects.filter()
    medicines = Medicine.objects.filter()
    context = {
        'ministered_medicines': ministered_medicines,
        'ministered_medicines_items': ministered_medicines_items,
        'patients': patients,
        'medicines': medicines
    }
    return render(request, template_name, context)

def delete_ministered_medicines(request, id_ministered_medicines):
    ministered_medicines = MinisteredMedicines.objects.get(id=id_ministered_medicines)
    ministered_medicines.delete()
    return redirect('ministered_medicines:list_ministered_medicines')

def add_ministered_medicines_item(request, id_ministered_medicines):
    template_name = 'ministered_medicines/add_ministered_medicines_item.html'
    context = {}
    if request.method == 'POST':
        form = MinisteredMedicineItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.ministered_medicines = MinisteredMedicines.objects.get(id=id_ministered_medicines)
            f.save()
            form.save_m2m()
            return redirect('ministered_medicines:list_ministered_medicines')
    form = MinisteredMedicineItemForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_ministered_medicines_item(request, id_ministered_medicines_item):
    ministered_medicinesitem = MinisteredMedicineItem.objects.get(id=id_ministered_medicines_item)
    ministered_medicinesitem.delete()
    return redirect('ministered_medicines:list_ministered_medicines')

def edit_ministered_medicines_status(request, id_ministered_medicines):
    template_name = 'ministered_medicines/edit_ministered_medicines_status.html'
    context ={}
    ministered_medicines = get_object_or_404(MinisteredMedicines, id=id_ministered_medicines)
    if request.method == 'POST':
        form = MinisteredMedicinesForm(request.POST, instance=ministered_medicines)
        if form.is_valid():
            form.save()
            return redirect('ministered_medicines:list_ministered_medicines')
    form = MinisteredMedicinesForm(instance=ministered_medicines)
    context['form'] = form
    return render(request, template_name, context)


