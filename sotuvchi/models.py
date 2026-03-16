from django.db import models

class mashinalar(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    
    # Yangi maydonlar (default qiymatlari bilan):
    transmission = models.CharField(max_length=50, default="Mexanika")
    engine_volume = models.IntegerField(default=0)
    year = models.IntegerField(default=2024)
    fuel_type = models.CharField(max_length=50, default="Benzin")
    turi = models.CharField(max_length=100, default="Sedan")