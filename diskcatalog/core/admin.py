from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Disk

#admin.site.register(Disk)
#class DiskAdmin(admin.ModelAdmin):
#    list_display = ('__str__', 'category', 'ra', 'dec', 'distance', 'system_age', 'central_star_mass', 'disk_major_axis', 'inclination', 'references')
#    search_fields = ('object', 'category', 'ra', 'dec', 'distance', 'system_age', 'central_star_mass', 'disk_major_axis', 'inclination', 'references')
#    list_filter = ('catalog',)

@admin.register(Disk)
class DiskAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'category', 'ra', 'dec', 'distance', 'system_age', 'central_star_mass', 'disk_major_axis', 'inclination', 'references')
    search_fields = ('object', 'category', 'ra', 'dec', 'distance', 'system_age', 'central_star_mass', 'disk_major_axis', 'inclination', 'references')
    list_filter = ('catalog',)
