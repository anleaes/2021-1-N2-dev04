from django.db import models
from patients.models import Patient

# Create your models here.

class MinisteredMedicines(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Medicamento Ministrado'
        verbose_name_plural = 'Medicamentos Ministrados'
        ordering =['-created_on']

    def __str__(self):
        return "%s" % (self.total_price) 


class MinisteredMedicinesItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    unitary_price = models.FloatField('Preco unitario',null=True, blank=True, default=0.0)
    ministered_medicines = models.ForeignKey(MinisteredMedicines, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Medicamento Ministrado'
        verbose_name_plural = 'Itens de Medicamento Ministrado'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.quantity) 

