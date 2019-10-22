# Generated by Django 2.2.6 on 2019-10-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disk',
            name='at_ref_wavelength',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='at_ref_wavelength'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='disk_diameter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='disk_diameter'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='disk_major_axis',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='disk_major_axis'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='distance',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='distance'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='inclination',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='inclination'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='r_band',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='r_band'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='resolution_elements_across',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='resolution_elements_across'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='spec_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='spec_type'),
        ),
    ]
