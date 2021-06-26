from django import forms
from .models import Anamnesis

class AnamnesisForm(forms.ModelForm):

    class Meta:
        model = Anamnesis
        exclude = ()