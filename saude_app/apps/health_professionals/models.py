from django.db import models
from specialties.models import Specialty

class HealthProfessional(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    crm = models.CharField('CRM', max_length=7)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    professional_specialty = models.ManyToManyField(Specialty, through='ProfessionalSpecialty', blank=True)

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering =['first_name']

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class ProfessionalSpecialty(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    health_professional = models.ForeignKey(HealthProfessional, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
        ordering =['id']

    def __str__(self):
        return self.specialty.name