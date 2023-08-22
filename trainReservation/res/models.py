from django.db import models


# Create your models here.
class Passenger(models.Model):
    category = models.CharField(max_length=122)
    Passengers = models.IntegerField()


# class Boogie(models.Model):
#     type = models.CharField(max_length=122)
#     seats = models.IntegerField()