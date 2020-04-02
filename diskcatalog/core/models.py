from django.db import models


class Disk(models.Model):
    Object = models.CharField(max_length=100, null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    SpecType = models.CharField(max_length=100, null=True, blank=True)
    Rband = models.CharField(max_length=100, null=True, blank=True)
    Distance = models.CharField(max_length=100, null=True, blank=True)
    DiskMajorAxis = models.CharField(max_length=100, null=True, blank=True)
    Inclination = models.CharField(max_length=100, null=True, blank=True)
    RA = models.CharField(max_length=100, null=True, blank=True)
    DEC = models.CharField(max_length=100, null=True, blank=True)
    SystemAge = models.CharField(max_length=100, null=True, blank=True)
    StellarMass = models.CharField(max_length=100, null=True, blank=True)
    References = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        ordering = ['Object']
        verbose_name = 'disk'
        verbose_name_plural = 'disks'

    def __str__(self):
        return self.Object
