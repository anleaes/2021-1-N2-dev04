from django.db import models
from patients.models import Patient
from anamnesis.models import Anamnesis
from vital_signs.models import VitalSign

class PatientEvolution(models.Model):
    patients = models.ForeignKey(Patient, on_delete=models.CASCADE)
    anamnesis =  models.ForeignKey(Anamnesis, on_delete=models.CASCADE)
    vital_signs =  models.ForeignKey(VitalSign, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Evolução Paciente'
        verbose_name_plural = 'Evoluções Paciente'
        ordering =['id']
