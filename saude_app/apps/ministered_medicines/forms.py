from django import forms
from .models import MinisteredMedicines, Patient, MinisteredMedicinesItem

class MinisteredMedicinesForm(forms.ModelForm):
    
    class Meta:
        model = MinisteredMedicines
        exclude = ('patient', 'created_on' , 'updated_on')

class MinisteredMedicinesItemForm(forms.ModelForm):
    
    class Meta:
        model = MinisteredMedicinesItem
        exclude = ('ministered_medicines', 'created_on' , 'updated_on')