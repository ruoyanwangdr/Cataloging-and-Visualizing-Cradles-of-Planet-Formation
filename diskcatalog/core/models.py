from django.db import models

class Disk(models.Model):
    object = models.CharField('object', max_length=100)
    category = models.CharField('category', max_length=100, null=True, blank=True)
    ra = models.CharField('ra', max_length=100, null=True, blank=True)
    dec = models.CharField('dec', max_length=100, null=True, blank=True)
    distance = models.CharField('distance', max_length=100, null=True, blank=True)
    system_age = models.CharField('system_age', max_length=100, null=True, blank=True)
    central_star_mass = models.CharField('central_star_mass', max_length=100, null=True, blank=True)
    disk_major_axis = models.CharField('disk_major_axis', max_length=100, null=True, blank=True)
    #disk_diameter = models.CharField('disk_diameter', max_length=100, null=True, blank=True)
    inclination = models.CharField('inclination', max_length=100, null=True, blank=True)
    #resolution_elements_across = models.CharField('resolution_elements_across', max_length=100, null=True, blank=True)
    #at_ref_wavelength = models.CharField('at_ref_wavelength', max_length=100, null=True, blank=True)
    references = models.CharField('references', max_length=10, null=True, blank=True)
    catalog = models.CharField('catalog', max_length=20, null=True, blank=True)

    class Meta:
        ordering = ('object',)
        verbose_name = 'disk'
        verbose_name_plural = 'disks'

    def __str__(self):
        return self.object
