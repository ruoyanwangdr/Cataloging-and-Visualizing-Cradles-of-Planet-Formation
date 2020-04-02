from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Disk


@admin.register(Disk)
class DiskAdmin(ImportExportModelAdmin):
    list_display = ('__str__',
                    'category',
                    'spec_type',
                    'r_band',
                    'distance',
                    'disk_major_axis',
                    'inclination',
                    'ra',
                    'dec',
                    'system_age',
                    'stellar_mass',
                    'references')
    search_fields = ('object',
                     'category',
                     'spec_type',
                     'r_band',
                     'distance',
                     'disk_major_axis',
                     'inclination',
                     'ra',
                     'dec',
                     'system_age',
                     'stellar_mass',
                     'references')
