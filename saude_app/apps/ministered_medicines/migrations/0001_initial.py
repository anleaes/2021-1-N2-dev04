# Generated by Django 3.2 on 2021-06-26 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinisteredMedicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('total_price', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Preco Total')),
                ('status', models.CharField(blank=True, choices=[('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado')], default='Em andamento', max_length=20, null=True, verbose_name='Status')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
            options={
                'verbose_name': 'Medicamento Ministrado',
                'verbose_name_plural': 'Medicamentos Ministrados',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='MinisteredMedicinesItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade')),
                ('unitary_price', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Preco unitario')),
                ('ministered_medicines', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ministered_medicines.ministeredmedicines')),
            ],
            options={
                'verbose_name': 'Item de Medicamento Ministrado',
                'verbose_name_plural': 'Itens de Medicamento Ministrado',
                'ordering': ['id'],
            },
        ),
    ]
