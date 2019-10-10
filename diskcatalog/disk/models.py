from django.db import models

class Resolved(models.Model):
    object = models.CharField(max_length=30)
    category = models.CharField(max_length=10)
    spectype = models.CharField(max_length=10)
    Rband = models.CharField(max_length=10)
    distance = models.CharField(max_length=10)
    diskmajoraxis = models.CharField(max_length=10)
    diskdiameter = models.CharField(max_length=10)
    inclination = models.CharField(max_length=10)
