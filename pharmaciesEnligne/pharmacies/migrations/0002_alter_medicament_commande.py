# Generated by Django 5.0.1 on 2024-01-09 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='commande',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacies.commande'),
        ),
    ]
