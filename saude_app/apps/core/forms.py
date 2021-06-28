from django import forms
from .models import Core, Patient

class CoreForm(forms.ModelForm):

    class Meta:
        model = Core
        exclude = ('created_on' , 'updated_on',)