from django import forms
from .models import health_professionals

class HealthProfessionalsForm(forms.ModelForm):

    class Meta:
        model = health_professionals
        exclude = ()