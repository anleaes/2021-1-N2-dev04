from django.db import models
from patients.models import Patient

# Create your models here.


class VitalSign(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    heart_rate = models.IntegerField('Frequência Cardíaca', default=0)
    respiratory_frequency = models.IntegerField('Frequência Respiratória', default=0)
    body_temperature = models.FloatField('Temperatura Corporal', default=0.0)    
    blood_pressure = models.CharField('Pressão Arterial', max_length=50)   
    date = models.DateField('Data dos Dados', auto_now=False, auto_now_add=False)    
    #date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Sinal Vital'
        verbose_name_plural = 'Sinais Vitais'
        ordering =['-created_on']

    def __str__(self):
        return "Sinais Vitais Paciente %s" % (self.patient) 
