from django.db import models
from django.db.models import SET_NULL


class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(CarBrand, on_delete=SET_NULL, null=True, related_name='cars')

    def __str__(self):
        return self.model