from django.db import models
from patients.models import Patient

class Core(models.Model):
    patients = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Core'
        verbose_name_plural = 'Core'
        ordering =['id']