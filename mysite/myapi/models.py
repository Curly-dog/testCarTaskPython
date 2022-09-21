from django.db import models

from django.db import models


# Create your models here.
class Car(models.Model):
    mark = models.CharField(max_length=80)
    numberOfDoor = models.IntegerField()
    registration = models.BooleanField()
