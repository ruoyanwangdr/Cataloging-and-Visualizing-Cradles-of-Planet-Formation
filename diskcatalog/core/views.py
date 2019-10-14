from django.shortcuts import render
from .models import Disk

def index(request):
    context = {}
    disk_list = Disk.objects.all()
    context['disk_list'] = disk_list
    return render(request, 'index.html', context)
