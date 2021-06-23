from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import VitalSignsForm
from .models import VitalSign , Patient

# Create your views here.


def add_vital_sign(request):
    template_name = 'vital_signs/add_vital_sign.html'
    context = {}
    if request.method == 'POST':
        form = VitalSignsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('vital_signs:list_vital_signs')
    form = VitalSignsForm()
    context['form'] = form
    return render(request, template_name, context)

def list_vital_signs(request):
    template_name = 'vital_signs/list_vital_signs.html'
    vital_signs = VitalSign.objects.filter()
    patients = Patient.objects.filter()
    context = {
        'vital_signs': vital_signs,
        'patients': patients,
    }
    return render(request, template_name, context)

def delete_vital_sign(request, id_vital_signs):
    vital_signs = VitalSign.objects.get(id=id_vital_signs)
    vital_signs.delete()
    return redirect('vital_signs:list_vital_signs')