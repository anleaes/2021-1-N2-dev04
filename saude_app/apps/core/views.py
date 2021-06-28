from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CoreForm
from .models import Core, Patient

@login_required(login_url='/autenticacao/login/')
def home(request):
    template_name ='core/home.html'
    patients = Patient.objects.filter()
    context = {
        'patients':patients
    }
    return render(request, template_name, context)

@login_required(login_url='/autenticacao/login/')
def search_clients(request):
    template_name = 'core/home.html'
    query = request.GET.get('query')
    patients = Patient.objects.filter(last_name__icontains=query)
    context = {
        'patients':patients
    }
    return render(request,template_name, context)