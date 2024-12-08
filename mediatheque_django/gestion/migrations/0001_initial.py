# Generated by Django 5.1.4 on 2024-12-06 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emprunteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bloque', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='JeuDePlateau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('createur', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('realisateur', models.CharField(max_length=200)),
                ('date_emprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dvds_empruntes', to='gestion.emprunteur')),
            ],
        ),
        migrations.CreateModel(
            name='Cd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('artiste', models.CharField(max_length=200)),
                ('date_emprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cds_empruntes', to='gestion.emprunteur')),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('auteur', models.CharField(max_length=200)),
                ('date_emprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='livres_empruntes', to='gestion.emprunteur')),
            ],
        ),
    ]