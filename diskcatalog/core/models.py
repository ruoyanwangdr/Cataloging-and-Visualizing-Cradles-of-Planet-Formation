from django.db import models

class Disk(models.Model):
    object = models.CharField('object', max_length=100)
    category = models.CharField('category', max_length=100)
    spec_type = models.CharField('spec_type', max_length=100)
    r_band = models.CharField('r_band', max_length=100)
    distance = models.CharField('distance', max_length=100)
    disk_major_axis = models.CharField('disk_major_axis', max_length=100)
    disk_diameter = models.CharField('disk_diameter', max_length=100)
    inclination = models.CharField('inclination', max_length=100)
    resolution_elements_across = models.CharField('resolution_elements_across', max_length=100)
    at_ref_wavelength = models.CharField('at_ref_wavelength', max_length=100)
    #references = models.CharField('references', max_length=10)
    if_resolved =(
        ('Resolved', 'Resolved'),
        ('Unresolved', 'Unresolved'),
    )
    catalog = models.CharField(
        'catalog',
        max_length=20,
        choices=if_resolved
    )

    class Meta:
        ordering = ('object',)
        verbose_name = 'disk'
        verbose_name_plural = 'disks'

    def __str__(self):
        return self.object
