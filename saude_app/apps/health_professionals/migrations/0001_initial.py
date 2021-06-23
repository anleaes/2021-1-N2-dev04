# Generated by Django 3.2.4 on 2021-06-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthProfessional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(max_length=7, verbose_name='CRM')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('address', models.CharField(max_length=200, verbose_name='Endereco')),
                ('cell_phone', models.CharField(max_length=20, verbose_name='Telefone celular')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('medical_speciality', models.CharField(max_length=50, verbose_name='Especialidade')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
                'ordering': ['id'],
            },
        ),
    ]