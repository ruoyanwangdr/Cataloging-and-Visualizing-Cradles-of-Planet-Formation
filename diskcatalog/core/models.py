from django.db import models

class Disk(models.Model):
    object = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True, blank=True)
    spec_type = models.CharField(max_length=100, null=True, blank=True)
    r_band = models.CharField(max_length=100, null=True, blank=True)
    distance = models.CharField(max_length=100, null=True, blank=True)
    disk_major_axis = models.CharField(max_length=100, null=True, blank=True)
    inclination = models.CharField(max_length=100, null=True, blank=True)
    ra = models.CharField(max_length=100, null=True, blank=True)
    dec = models.CharField(max_length=100, null=True, blank=True)
    system_age = models.CharField(max_length=100, null=True, blank=True)
    stellar_mass = models.CharField(max_length=100, null=True, blank=True)
    references = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        ordering = ('object',)
        verbose_name = 'disk'
        verbose_name_plural = 'disks'

    def __str__(self):
        return self.object
