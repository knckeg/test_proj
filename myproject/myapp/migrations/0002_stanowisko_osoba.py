# Generated by Django 5.1.4 on 2025-01-02 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('plec', models.CharField(choices=[('kobieta', 'Kobieta'), ('mezczyzna', 'Mężczyzna'), ('inne', 'Inne')], max_length=10)),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='osoby', to='myapp.stanowisko')),
            ],
        ),
    ]
