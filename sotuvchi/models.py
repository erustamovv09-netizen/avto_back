from django.db import models

# Create your models here.
class mashinalar(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    transmission = models.CharField
    engine_volume = models.IntegerField
    year = models.IntegerField
    fuel_type = models.CharField
    turi = models.CharField