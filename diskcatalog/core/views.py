from django.shortcuts import render
from .models import Disk
import os


def index(request):
    context = {}
    disk_list = Disk.objects.all()
    context['disk_list'] = disk_list
    return render(request, 'index.html', context)


#def index(request):
#    module_dir = os.path.dirname(__file__)
#    file_path = os.path.join(module_dir, 'data.txt')
#    disk_list = open(file_path , 'r')
#    data = data_file.read()
#    context = {'disk_list': data}
#    return render(request, 'index.html', context)
