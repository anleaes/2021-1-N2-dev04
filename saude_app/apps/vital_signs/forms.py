from django import forms
from .models import VitalSign, Patient

class VitalSignsForm(forms.ModelForm):
    
    class Meta:
        model = VitalSign
        exclude = ('created_on' , 'updated_on')