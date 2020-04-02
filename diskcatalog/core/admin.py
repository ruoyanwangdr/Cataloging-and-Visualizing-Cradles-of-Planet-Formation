from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Disk


@admin.register(Disk)
class DiskAdmin(ImportExportModelAdmin):
    list_display = ('Object',
                    'Category',
                    'Spec Type',
                    'R band',
                    'Distance',
                    'Disk Major Axis',
                    'Inclination',
                    'RA',
                    'DEC',
                    'System Age',
                    'Stellar Mass',
                    'References')
    search_fields = ('object',
                     'category',
                     'spectype',
                     'rband',
                     'distance',
                     'diskmajoraxis',
                     'inclination',
                     'ra',
                     'dec',
                     'systemage',
                     'stellarmass',
                     'references')
