# Generated by Django 3.2.4 on 2021-06-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(max_length=100, verbose_name='Descricao')),
                ('date_fabrication', models.DateField(verbose_name='Data Fabricacao')),
                ('is_active', models.BooleanField(default=False, verbose_name='Ativo')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Foto')),
                ('doc', models.FileField(upload_to='docs', verbose_name='Documentos')),
            ],
            options={
                'verbose_name': 'Medicine',
                'verbose_name_plural': 'Medicines',
                'ordering': ['id'],
            },
        ),
    ]