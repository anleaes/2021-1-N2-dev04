from django import forms
from .models import HealthProfessional

class HealthProfessionalsForm(forms.ModelForm):

    class Meta:
        model = HealthProfessional
        exclude = ()