from django.db import models

class Car(models.Model):
    MANUFACTURERS = (
        ('BMW', 'bmw'),
        ('AUDI', 'audi'),
        ('TESLA', 'tesla'),
        ('MERCEDES' ,'mercedes')
    )
    manufacturer = models.CharField(max_length=128, choices=MANUFACTURERS)
    model = models.CharField(max_length=128)
    year = models.IntegerField()
    color = models.CharField(max_length=128)
    TRANSMISSION = (
        ('MECHANIC', 'mechanic'),
        ( 'AUTO', 'auto'),
        ('ROBOT', 'robot'),    
    )
    transmission = models.CharField(max_length=20, choices = TRANSMISSION)
    