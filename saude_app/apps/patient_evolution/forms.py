from django import forms
from .models import PatientEvolution, Patient, VitalSign, Anamnesis

class PatientEvolutionForm(forms.ModelForm):

    class Meta:
        model = PatientEvolution
        exclude = ('created_on' , 'updated_on',)