from django.contrib import admin
from .models import Disk

admin.site.register(Disk)
class DiskAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category', 'spec_type', 'r_band', 'distance', 'disk_major_axis', 'disk_diameter', 'inclination', 'resolution_elements_across', 'at_ref_wavelength')
    search_fields = ('object', 'category', 'spec_type', 'r_band', 'distance', 'disk_major_axis', 'disk_diameter', 'inclination', 'resolution_elements_across', 'at_ref_wavelength')
    list_filter = ('catalog',)
