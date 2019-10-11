from django.http import HttpResponse
from .models import Resolved
from django.shortcuts import render

def index(request):
    all_resolved = Resolved.objects.all()
    context = {'all_resolved' : all_resolved}
    return render(request, 'disk/index.html', context)


def detail(request, resolved_id):
    return HttpResponse("<h2>Details for resolved disks: " + str(resolved_id) + "</h2>")
