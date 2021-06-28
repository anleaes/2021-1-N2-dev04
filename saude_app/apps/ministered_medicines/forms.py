from django import forms
from .models import MinisteredMedicines, Patient, MinisteredMedicineItem, Medicine

class MinisteredMedicinesForm(forms.ModelForm):
    
    class Meta:
        model = MinisteredMedicines
        exclude = ('patient', 'created_on' , 'updated_on')

class MinisteredMedicineItemForm(forms.ModelForm):
    
    class Meta:
        model = MinisteredMedicineItem
        exclude = ('ministered_medicines', 'created_on' , 'updated_on')