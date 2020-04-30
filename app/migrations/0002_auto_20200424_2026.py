# Generated by Django 3.0.4 on 2020-04-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.CharField(choices=[('BMW', 'bmw'), ('AUDI', 'audi'), ('TESLA', 'tesla'), ('MERCEDES', 'mercedes')], max_length=128),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('MECHANIC', 'mechanic'), ('AUTO', 'auto'), ('ROBOT', 'robot')], max_length=20),
        ),
    ]
