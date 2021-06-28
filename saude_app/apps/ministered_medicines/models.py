from django.db import models
from patients.models import Patient
from medicines.models import Medicine

class MinisteredMedicines(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ministered_medicine_item = models.ManyToManyField(Medicine, through='MinisteredMedicineItem', blank=True)
    class Meta:
        verbose_name = 'Medicamento Ministrado'
        verbose_name_plural = 'Medicamentos Ministrados'
        ordering =['-created_on']

    def __str__(self):
        return "%s" % (self.patient.first_name) 

class MinisteredMedicineItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    ministered_medicines = models.ForeignKey(MinisteredMedicines, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Medicamento Ministrado'
        verbose_name_plural = 'Itens de Medicamento Ministrado'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.quantity) 

