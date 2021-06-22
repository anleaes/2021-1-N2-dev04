from django import forms
from .models import Anamnesis, Patient, HealthProfessional

class AnamnesisForm(forms.ModelForm):

    class Meta:
        model = Anamnesis
        exclude = ()