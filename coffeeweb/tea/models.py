from django.db import models

class Teaa(models.Model):
    name = models.CharField(max_length=100)
    taste = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    image = models.CharField(max_length=500)

class Coffee(models.Model):
    coffeename = models.ForeignKey(Teaa, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
