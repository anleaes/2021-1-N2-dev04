from django.db import models

class Patient(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    birth = models.DateField('Data de Nascimento', max_length= 10)
    heigt = models.DecimalField('Altura', max_digits=4, decimal_places=2, default=0.00)
    weight = models.DecimalField('Peso', max_digits=6, decimal_places=2, default=0.00)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering =['first_name']

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
