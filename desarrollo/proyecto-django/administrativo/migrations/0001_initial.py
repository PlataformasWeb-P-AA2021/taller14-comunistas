# Generated by Django 3.2.4 on 2021-06-26 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre de edificio')),
                ('direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('ciudad', models.CharField(max_length=30, verbose_name='Ciudad')),
                ('tipo', models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propietario', models.CharField(max_length=30, verbose_name='Nombre de propietario')),
                ('costoDep', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Costo de departamento')),
                ('numCuartos', models.IntegerField(verbose_name='Numero de cuartos')),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='administrativo.edificio')),
            ],
        ),
    ]