from django.db import models
from patients.models import Patient
from health_professionals.models import HealthProfessional

# Create your models here.

class Anamnesis(models.Model):
    patients = models.ForeignKey(Patient, on_delete=models.CASCADE)
    health_professional = models.ForeignKey(HealthProfessional, on_delete=models.CASCADE)
    main_complaint =  models.CharField('Queixa', max_length=200)
    allergies =  models.CharField('Alergias', max_length=200)
    habits =  models.CharField('Habitos de Vida', max_length=200)
    family_history = models.CharField('Histórico Familiar', max_length=200)
    date = models.DateField('Data', auto_now=False, auto_now_add=False) 

    class Meta:
        verbose_name = 'Anamnese'
        verbose_name_plural = 'Anamneses'
        ordering =['date']